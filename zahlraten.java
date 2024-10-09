
import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;

public class zahlraten {

    static Integer meinZahl = ThreadLocalRandom.current().nextInt(0, 100 + 1);

    public static void main(String[] args) 
    {
        System.out.println(meinZahl);
        userInput();
    }

    public static void userInput() {
        Scanner userInputScanner = new Scanner(System.in);
        System.out.print("Bitte gebe eine Zahl ein: ");
        Integer zahl = userInputScanner.nextInt();
        raten(zahl);
        userInputScanner.close();
    }


    public static void raten(Integer number) {
        if (number == meinZahl) {
            System.out.print("Du hast richtig geranten\n ");
        } else {
            System.out.print("Du hast falsh geraten \n");
        }
    }

}

    