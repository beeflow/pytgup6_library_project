create table publisher
(
    publisher_id   int auto_increment,
    publisher_name varchar(100),
    primary key (publisher_id)
);

create table book
(
    book_id           int auto_increment,
    book_title        varchar(100) not null,
    book_isbn         varchar(13),
    book_description  varchar(4000),
    book_publisher_id int          not null,

    primary key (book_id),

    foreign key (book_publisher_id) references
        publisher (publisher_id)
        on delete restrict on update cascade
);

create table author
(
    author_id   int auto_increment,
    author_name varchar(150),

    primary key (author_id)
);

create table book_author
(
    book_id   int not null,
    author_id int not null,

    primary key (book_id, author_id),
    foreign key (book_id) references book (book_id)
        on delete restrict on update cascade,
    foreign key (author_id) references author (author_id)
        on delete restrict on update cascade
);

create table book_copy
(
    bc_id        int auto_increment,
    bc_condition enum ('good', 'bad', 'terrible'),
    is_available bool not null,
    bc_book_id   int  not null,

    primary key (bc_id),
    foreign key (bc_book_id) references book (book_id)
        on delete restrict on update cascade
);

create table library_client
(
    lc_id   int auto_increment,
    lc_name varchar(150) not null,

    primary key (lc_id)
);
create table rent_book
(
    rb_id          int auto_increment,
    rb_rent_date   datetime not null default now(),
    rb_return_date datetime null,
    rb_bc_id       int      not null comment 'Book copy ID',
    rb_lc_id       int      not null comment 'Library client ID',

    primary key (rb_id),
    foreign key (rb_bc_id) references book_copy (bc_id)
        on delete restrict on update cascade,
    foreign key (rb_lc_id) references library_client (lc_id)
        on delete restrict on update cascade
);

create table first_name
(
    fn_id      int auto_increment,
    first_name varchar(20),

    primary key (fn_id)
);

create table last_name
(
    ln_id     int auto_increment,
    last_nama varchar(50),
    primary key (ln_id)
);

alter table last_name
    change last_nama last_name varchar(50);

insert into author(author_name)
values ('Henryk Sienkiewicz'),
       ('Adam Mickiewicz'),
       ('Steven King'),
       ('Homer');
insert into author(author_name)
values ('Henryk Konopko');

select author_id, author_name
from author;

alter table author
    add author_first_name_id int null;
alter table author
    add author_last_name_id int null;

alter table author
    add constraint author_first_name_id_fk
        foreign key (author_first_name_id) references first_name (fn_id)
            on update cascade on delete restrict;

alter table author
    add constraint author_last_name_id_fk
        foreign key (author_last_name_id) references last_name (ln_id)
            on update cascade on delete restrict;

alter table first_name
    add constraint first_name_unique unique (first_name);
alter table last_name
    add unique (last_name);

select SUBSTRING_INDEX(author_name, ' ', 1)  as first_name,
       SUBSTRING_INDEX(author_name, ' ', -1) AS last_name
from author;

insert ignore into last_name(last_name)
select distinct SUBSTRING_INDEX(author_name, ' ', -1)
from author;

select last_name
from last_name;

insert into first_name (first_name)
select distinct SUBSTRING_INDEX(author_name, ' ', 1)
from author;

select fn_id, first_name
from first_name;

SET SQL_SAFE_UPDATES = 0;

update author
set author_first_name_id = (
    select fn_id
    from first_name
    where first_name = SUBSTRING_INDEX(author_name, ' ', 1)
),
    author_last_name_id  = (
        select ln_id
        from last_name
        where last_name = SUBSTRING_INDEX(author_name, ' ', -1)
    );

select author.*,
       first_name,
       last_name
from author
         left outer join first_name on author_first_name_id = fn_id
         left outer join last_name on author_last_name_id = ln_id;

alter table author
    drop column author_name;

insert into library_client (lc_name)
values ('Henryk Sienkiewicz'),
       ('Steven Mickiewicz'),
       ('Henryk King'),
       ('Adam Konopko'),
       ('Jurand Zespychowa'),
       ('Agnieszka Niewiem');

insert ignore into last_name(last_name)
select distinct SUBSTRING_INDEX(lc_name, ' ', -1)
from library_client;

insert ignore into first_name (first_name)
select distinct SUBSTRING_INDEX(lc_name, ' ', 1)
from library_client;


alter table library_client
    add lc_first_name_id int null;
alter table library_client
    add lc_last_name_id int null;

alter table library_client
    add constraint lc_first_name_id_fk
        foreign key (lc_first_name_id) references first_name (fn_id)
            on update cascade on delete restrict;

alter table library_client
    add constraint lc_last_name_id_fk
        foreign key (lc_last_name_id) references last_name (ln_id)
            on update cascade on delete restrict;

update library_client
set lc_first_name_id = (
    select fn_id
    from first_name
    where first_name = SUBSTRING_INDEX(lc_name, ' ', 1)
),
    lc_last_name_id  = (
        select ln_id
        from last_name
        where last_name = SUBSTRING_INDEX(lc_name, ' ', -1)
    );

alter table library_client
    drop column lc_name;


create view v_library_client as
select lc_id,
       first_name,
       last_name
from library_client
         left outer join first_name
                         on fn_id = lc_first_name_id
         left outer join last_name
                         on ln_id = lc_last_name_id;

create view v_author as
select author_id,
       first_name,
       last_name
from author
         left outer join first_name on author_first_name_id = fn_id
         left outer join last_name on author_last_name_id = ln_id;

select *
from v_library_client;
select *
from v_author;

create function f_add_first_name(firstName varchar(20))
    returns int DETERMINISTIC
    READS SQL DATA
begin
    if (select fn_id from first_name where lower(first_name) = lower(firstName)) is null then
        insert into first_name(first_name) values (firstName);
    end if;

    return (select fn_id from first_name where lower(first_name) = lower(firstName));
end;

create function f_add_last_name(lastName varchar(20))
    returns int DETERMINISTIC
    READS SQL DATA
begin
    if (select ln_id from last_name where lower(last_name) = lower(lastName)) is null then
        insert into last_name(last_name) values (lastName);
    end if;

    return (select ln_id from last_name where lower(last_name) = lower(lastName));
end;

insert into library_client(lc_first_name_id, lc_last_name_id)
values (f_add_first_name('Wania'), f_add_last_name('Cichobzdziejew'));

drop trigger if exists trg_rent_a_book;
create trigger trg_rent_a_book
    after insert
    on rent_book
    for each row
begin
    update book_copy set is_available = 0 where bc_id = NEW.rb_bc_id;
end;

drop trigger if exists trg_return_book;
create trigger trg_return_book
    after update
    on rent_book
    for each row
begin
    if (
                (select is_available from book_copy where bc_id = NEW.rb_bc_id) = 0
            and OLD.rb_return_date is null
            and NEW.rb_return_date is not null
        ) then
        update book_copy set is_available = 1 where bc_id = NEW.rb_bc_id;
    end if;
end;

drop trigger if exists trg_return_date_hodor;
create trigger trg_return_date_hodor
    before update
    on rent_book
    for each row
begin
    if (new.rb_return_date <= OLD.rb_rent_date) then
        SIGNAL SQLSTATE '45000' SET
            MYSQL_ERRNO = 37455,
            MESSAGE_TEXT = 'Error: Nie można oddać książki przed datą wypożyczenia!';
    end if;

    if (new.rb_return_date > now()) then
        SIGNAL SQLSTATE '45000' SET
            MYSQL_ERRNO = 37465,
            MESSAGE_TEXT = 'Error: Nie można oddać książki z późniejszą datą!';
    end if;
end;

CREATE TRIGGER trg_rent_book_status_replacement
    AFTER UPDATE
    ON book_copy
    FOR EACH row
BEGIN
    if (old.is_available = 0 and NEW.is_available = 1) then
        update rent_book
        set rb_return_date = now()
        where rb_bc_id = OLD.bc_id
        and rb_return_date is null;
    end if;
end;

alter table book_author rename book_author_through;