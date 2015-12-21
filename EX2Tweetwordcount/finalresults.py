from sys import argv
import psycopg2

def queryer(word):
	"""
	Takes in a word as sys argument and checks Tweetwordcount database and outputs the count.
	"""
	conn = psycopg2.connect(database="tcount", user="postgres", password="password", host="localhost", port="5432")
	cur = conn.cursor()
	query = cur.mogrify("SELECT count FROM Tweetwordcount WHERE word = %s", (word,))
	cur.execute(query)
	count = cur.fetchall()
	if count:
		result = count[0][0]
	else:
		result = 0
	return result

def lister():
	"""
	Lists out all words in the db with their counts.
	"""
	conn = psycopg2.connect(database="tcount", user="postgres", password="password", host="localhost", port="5432")
	cur = conn.cursor()
	cur.execute("SELECT * FROM Tweetwordcount")
	output = cur.fetchall()
	output.sort()
	print str(output)[1:-1]
	return output


if __name__== "__main__":
	if len(argv) == 1:
		lister()
	else:
		for a in argv[1:]:
			print "Total number of occurences of \"%s\": " %a + str(queryer(a))