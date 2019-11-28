use overbejt;

drop table gene;
drop table source;
drop table features;
drop table attr;

create table source(
    source_id INT not null AUTO_INCREMENT,
    source_name varchar(255) not null,
    PRIMARY KEY ( source_id, source_name),
    INDEX (source_id, source_name)
);
create table features(
    feature_id INT not null AUTO_INCREMENT,
    feature varchar(255) not null,
    PRIMARY KEY (feature_id, feature)
);
create table attr(
    attr_id int not null AUTO_INCREMENT,
    data varchar(255) not null,
    PRIMARY KEY (attr_id, data),
    INDEX (attr_id, data)
);
create table gene(
   gene_id INT NOT NULL AUTO_INCREMENT,
   seqname varchar(255) not null,
   g_start int not null,
   g_end int not null,
   score int,
   frame int,
   a_id int,
   f_id int,
   s_id int,
   PRIMARY KEY (gene_id),
   foreign key (a_id) references attr(attr_id),
   foreign key (f_id) references features(feature_id),
   foreign key (s_id) references source(source_id),
   INDEX (gene_id, seqname, g_start, g_end, score, frame, a_id, f_id, s_id)
);
