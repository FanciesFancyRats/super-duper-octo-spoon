import java.util.Scanner;

public class p1b {


  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int month = 0;
    int round = 0;
    double flRound = 0;

    double increment;
    double balance;
    double updateBalance = 1;
    double air;
    double monthlyPayment = 0;
    double monthlyIntrest;
    double intrestPaid;
    double principalPaid;
    double balanceCheck = 100;

    System.out.print("Please enter the payment increment: ");
    increment = sc.nextDouble();
    System.out.print("Please enter the outstanding balance: ");
    balance = sc.nextDouble();
    System.out.print("Please enter the annual intrest rate: ");
    air = sc.nextDouble();

    monthlyIntrest = air / 12d;

    while(balanceCheck > 0){

      monthlyPayment = monthlyPayment + increment;
      updateBalance = balance;
      month = 0;

      while(month < 12 && updateBalance > 0){

        intrestPaid = air/12 * updateBalance;
        principalPaid = monthlyPayment - intrestPaid;
        updateBalance = updateBalance*(1 + monthlyIntrest) - monthlyPayment;
        month++;
      //System.out.print("\n We are trying to solve... ");
      // System.out.print(month);

      }
      balanceCheck = updateBalance;
      System.out.print("\nI am trying to solve...");
      System.out.print(updateBalance);
    }

    System.out.print("\n *** Solved ***");
    System.out.print("\n Monthly payment: ");
    flRound = monthlyPayment;
    flRound = flRound
    System.out.print(monthlyPayment);
    System.out.print("\n Number of months needed: ");
    System.out.print(month);
    flRound = updateBalance;
    flRound = flRound - 0.005;
    flRound = flRound * 100;

    round = (int)(flRound);
    flRound = round;
    flRound = flRound/100d;
    updateBalance = flRound;


    System.out.print("\n Balance: ");
    System.out.print(updateBalance);
    //System.out.println(flRound);
    //System.out.println(round);





    //while(balanceCheck > 0){


  //  }

  }
}
