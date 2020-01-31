#this scripts does extract and load from postgres to SQL Sever

import psycopg2,pyodbc,datetime



def main():
    
    sql_con = pyodbc.connect('Driver={SQL Server};Server=servername;Database=datavase;Trusted_Connection=yes;')
    sql_cursor = sql_con.cursor()
    
    conn = psycopg2.connect(
            database='database name',
            user ="user_name",
            password = 'password',
            host ='10.*.*.*',
            port='54**'
            )
    cursor = conn.cursor()
    cursor.execute("Select  * from table where condition  ")
    #print('The number of record is {}',format(cursor.fetchone()[0]))
    result_set = cursor.fetchall()
    #field_name = cursor.description
    #for x in field_name:
       # print(x[0])
    st= datetime.datetime.now()
    print(st)
    for row in result_set:
        print(row[2] + "_" + str(row[11]))
        sql_cursor.execute("select count(*) from table name where coondition ", row[2] )
        if sql_cursor.fetchone()[0] == 0:
            sql_cursor.execute("insert into  table  ([filed1],[field2,[field3],[packaged_volume],[field4],[field5]) values(?,?,?,?,?,?,?)", row[1],row[2],row[3],row[4],row[5],row[7]])
            sql_con.commit()

        else:
            sql_cursor.execute("update PCD_Bulk_Inventory set [name] = (?) ,[Batch_id] = (?),[current_weight] = (?) , [packaged_weight] = (?) ,[packaged_volume] = (?) ,[status]=(?),[archived] = (?) where [batch_id] = (?)",row[1],row[2],row[3],row[4],row[5],row[7],row[11],row[2])

            sql_con.commit()
   
        
    ed = datetime.datetime.now()

    
    
                
if __name__ == '__main__':
    main()
