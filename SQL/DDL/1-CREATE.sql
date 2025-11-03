CREATE TABLE ofertas 
(disc_cod  numeric(5)  not null, 
 prof_matr  numeric(5)  not null, 
 oferta_sem   char(1)        not null, 
 oferta_ano  char(4)        not null);


CREATE VIEW v_professores 
(matricula, nome) 
as 
(SELECT prof_matr, prof_nome  
  FROM professores 
  WHERE prof_ds_dou is null)