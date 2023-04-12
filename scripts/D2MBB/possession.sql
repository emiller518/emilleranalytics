SELECT * from Game Where HomeID = 1 AND SeasonID = 15;


-- Where the final free throw is made
SELECT a.*, b.PlayTypeID FROM (
SELECT GameID, Half, Time, max(PlayNum) as playnum From PlayByPlay WHERE GameID = 201911091 and PlayTypeID IN (14,15) GROUP BY GameID, Half, Time
)a INNER JOIN
(SELECT Half, PlayNum, Time, Seconds, PlayTypeID From PlayByPlay WHERE GameID = 201911091)b 
ON a.Half = b.Half and a.playnum = b.PlayNum and a.Time = b.Time
WHERE b.PlayTypeID = 14
order by a.half asc, b.seconds desc;


-- And 1 situations. Made basket, then foul
SELECT a.*, b.* FROM 
(
SELECT * From PlayByPlay WHERE GameID = 201911091
) a
INNER JOIN
(
SELECT * From PlayByPlay WHERE GameID = 201911091
) b
on a.half = b.half
and a.PlayNum = b.PlayNum-1
and a.Seconds = b.Seconds
WHERE a.PlayTypeID in (8,9,10,11,13) and b.PlayTypeID = 22





-- This is the easy part. Typical plays that end a possession. Made baskets, turnovers, defensive rebounds
UPDATE PlayByPlay SET Posession = 1 where PlayTypeID in (8,9,10,11,13,17,21)


-- Count the last made free throw as a possession
UPDATE PlayByPlay b
INNER JOIN ( SELECT GameID, Half, Time, max(PlayNum) as playnum From PlayByPlay WHERE PlayTypeID IN (14,15) GROUP BY GameID, Half, Time ) a
ON a.Half = b.Half and a.playnum = b.PlayNum and a.Time = b.Time and a.GameID = b.GameID
SET Posession = 1
WHERE b.PlayTypeID = 14


-- For "And 1" situations, shooting foul after made basket, do not count the made basket as a possession
UPDATE PlayByPlay SET Posession = 0 WHERE PlayByPlayID in (
SELECT pbp.* FROM (
select PlayByPlayID from PlayByPlay
where(GameID, half, PlayNum , Seconds) IN
(SELECT GameID, half, PlayNum - 1 prevplay, Seconds
FROM PlayByPlay
WHERE PlayTypeID = 22 )
AND PlayTypeID in (8,9,10,11,13)) pbp )
