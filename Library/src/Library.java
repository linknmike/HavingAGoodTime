import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Library {

    HashMap<String, BookInformation> Books = new HashMap<String, BookInformation>();
    public Library() {
        BookInformation a = new BookInformation(1000, true);
        Books.put("The Way of Kings", a);
        BookInformation b = new BookInformation(150, true);
        Books.put("Textbook", b);
    }
    //vector<int>name
    void examine(String book) {
        System.out.println(Books.get(book).pageCount);
        System.out.println(Books.get(book).here);
    }
    void checkOut(String book) {
        Books.get(book).here = false;
        System.out.println(book + " is now checked out.");
    }
    void checkIn(String book) {
        Books.get(book).here = true;
        System.out.println(book + " is now checked in.");
    }
    void tearOutPages(String book, int howMany){
        Books.get(book).pageCount -= howMany;
        System.out.println(book + " now has " + howMany + " fewer pages. It now has " + Books.get(book).pageCount + ". Nice going, asshole.");
    }
    void donate(String book, int pages) {
        BookInformation a = new BookInformation(pages, true);
        Books.put(book, a);
        System.out.println(book + " has been added to the library. It has " + pages + " pages.");
    }

    public static void main(String [ ] args) {
        Library liberry = new Library();
        liberry.examine("The Way of Kings");
        liberry.checkOut("The Way of Kings");
        liberry.checkIn("The Way of Kings");
        liberry.tearOutPages("The Way of Kings", 999);
        liberry.donate("Necronomicon", 120);

    }
}

