install.packages("RPostgreSQL")
install.packages("ggplot2")
require("RPostgreSQL")
require("ggplot2")
# create a connection
# save the password that we can "hide" it as best as we can by collapsing it
pw <- {
  "password"
}

# loads the PostgreSQL driver
drv <- dbDriver("PostgreSQL")
# creates a connection to the postgres database
# note that "con" will be used later in each connection to the database
con <- dbConnect(drv, dbname = "tcount",
                 host = "localhost", port = 5432,
                 user = "postgres", password = pw)
rm(pw) # removes the password

dbExistsTable(con, "tweetwordcount")
df_postgres <- dbGetQuery(con, "SELECT * from tweetwordcount ORDER BY count desc LIMIT 20")

df_postgres$ordered_word <-factor(df_postgres$word, levels=df_postgres[order(df_postgres$count),"word"])

#plot
tweets_plot <- ggplot(df_postgres, aes(ordered_word, count)) 
tweets_plot + geom_bar(stat="identity", fill="#56B4E9", colour="black") + 
  ggtitle("Top 20 Most Frequent Words in my Twitter Feed") + coord_flip() + 
  ylab("Counts") + xlab("Word")

