-- Em 11.sql, escreva uma consulta SQL para listar os títulos dos cinco filmes com melhor classificação (em ordem)
   --que Chadwick Boseman estrelou, começando com os de maior classificação.
-- Sua consulta deve gerar uma tabela com uma única coluna para o título de cada filme.
-- Você pode presumir que há apenas uma pessoa no banco de dados com o nome Chadwick Boseman.


SELECT movies.title FROM people
JOIN stars ON people.id = stars.person_id JOIN movies ON stars.movie_id = movies.id JOIN ratings ON movies.id = ratings.movie_id
WHERE people.name = "Chadwick Boseman" ORDER BY rating DESC LIMIT 5;


