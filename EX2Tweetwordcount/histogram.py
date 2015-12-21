from sys import argv
import psycopg2

def hist(k1, k2):
	"""
	Takes in 2 numbers as sys arguments and outputs all word-count pairs that is greater than or equal to the smaller number and less than the second number.
	"""
	conn = psycopg2.connect(database="tcount", user="postgres", password="password", host="localhost", port="5432")
	cur = conn.cursor()
	query = cur.mogrify("SELECT * FROM Tweetwordcount WHERE count BETWEEN %s AND %s ORDER BY count", (k1,k2-1))
	cur.execute(query)
	results = cur.fetchall()
	for x in results:
		print str(x[0]) + ': ' + str(x[1])
	return results

if __name__== "__main__":
	hist(int(argv[1]), int(argv[2]))