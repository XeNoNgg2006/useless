import java.util.Scanner;



public class birthdayToAge {
    public static void main (String[] args)
    {
     userInputBirthday();
    }

    public static void userInputBirthday()
    {
        Scanner inputBirthday = new Scanner(System.in);
        System.out.print("Geben Sie Ihren Geburtstag ein (z.B: 12.05.2000): ");
        String birthday = inputBirthday.nextLine();
        calculateAge(birthday);
        inputBirthday.close();
    }


    public static void calculateAge(String birthday) {
        int birthdayNumbers = Integer.parseInt(birthday.replaceAll("\\D", ""));
        int birthYear = birthdayNumbers % 10000;
        birthdayNumbers = birthdayNumbers / 10000;
        int birthMonth = birthdayNumbers % 100;
        birthdayNumbers = birthdayNumbers / 100;
        int birthDay = birthdayNumbers;
        
        int ageYear = 2023 - birthYear;
        int ageMonth = 0;
        int ageDays = 0;
        if (birthMonth > 10) {
            ageYear = ageYear - 1;
            ageMonth = 12 - (birthMonth - 10);
        } else if (birthMonth < 10) {
            ageMonth = 10 - birthMonth;
        } else {
            ageMonth = 0;
        }

        if (birthDay < 23) {
            ageDays = 23 - birthDay;
        } else if (birthDay > 23) {
            ageMonth -= 1;
            ageDays = 30 - (23 - birthDay);
        } else {
            ageDays = 0;
        }
        System.out.println("You are " + ageYear + " years " + ageMonth + " Months " + ageDays + " Days old");
    }
}

