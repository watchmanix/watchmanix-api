create table if not exists monitors (
    id integer primary key autoincrement not null,
    name text,
    created_at timestamp default current_timestamp not null,
    updated_at timestamp default current_timestamp not null
);

INSERT INTO monitors (id, name) VALUES (1, "Stone Gilliam");
INSERT INTO monitors (id, name) VALUES (2, "Julie Fields");
INSERT INTO monitors (id, name) VALUES (3, "Lynn Pope");
INSERT INTO monitors (id, name) VALUES (4, "Henry Wilson");
INSERT INTO monitors (id, name) VALUES (5, "Ruby Bennett");
