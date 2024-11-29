def main():


 try:
   bookslist = []
   infile = open("bookslist","r")
   line = infile.readline()
   while line:
     bookslist.append(line.strip("\n").split(","))
     line = infile.readline()
   infile.close()  

 except FileNotFoundError :
   print ("The <bookslist.txt> file is not found ") 
   print("starting a new book list")
   bookslist = []

   choice = 0
   while choice !=4:
    print("*** Books Manger ***")
    print("1) add a Book")
    print("2) Lookup a book")
    print("3) Display books")
    print("4)Quit")
    choice = int(input())



    if choice == 1:
      print("addig a book...")
      nBook = input("Enter the name of the book>>>>>")
      nAuthor = input("Enter the name of the Author>>>>>")
      nPages = input("Enter the number of  pages  >>>>>")

      bookslist.append([nBook,nAuthor,nPages])

    elif choice == 2:
      print("Looking up for a book.....")
      keyword = input("Enter Search term: ")
      for book in bookslist:
        if keyword in book:
          print(book)

    elif choice == 3:
       print("Displaying all Books....")
       for i in range(len(bookslist)):
         print(bookslist[i])
    elif choice == 4:
      print("Quitting program")
    print("program Terminated!")      


   with open("bookslist.txt", "w") as outfile:
        for book in bookslist:
            outfile.write(",".join(book) + "\n")
   print("Program terminated!")


if __name__ == "__main__" :
 main()

