#include <iostream>
using namespace std;

void showMenu()
{
    cout << "********MENU********" << endl;
    cout << "1. Check Balance" << endl;
    cout << "2. Deposit" << endl;
    cout << "3. Withdraw" << endl;
    cout << "4. Money Transfer" << endl;
    cout << "5. Exit" << endl;
    cout << "********************" << endl;
}

int main()
{
    // check balance, deposit, withdraw, show menu
    int option;
    double balance = 1500;

    do
    {
        showMenu();
        cout << "Option: ";
        cin >> option;
        system("cls");
        switch (option)
        {
        case 1:
            cout << "Balance is: $" << balance << endl;
            break;
        case 2:
            cout << "Deposit amount: ";
            double depositAmount;
            cin >> depositAmount;
            balance += depositAmount;
            break;
        case 3:
            cout << "Withdraw amount: ";
            double WithdrawAmount;
            cin >> WithdrawAmount;
            if (WithdrawAmount <= balance)
                balance -= WithdrawAmount;
            else
                cout << "Not enough money" << endl;
            break;
        case 4:
            cout << "Enter 8 digit account number: ";
            string AccountNumber = "";
            cin >> AccountNumber;
            if (AccountNumber.length() > 8 || AccountNumber.length() < 8)
            {
                cout << "Invalid Account Number" << endl;
                break;
            }
            cout << "How much amount you want to transfer:$ ";
            double TransferAmount;
            cin >> TransferAmount;
            cout << "Amount Transfered" << endl;
            if (TransferAmount <= balance)
                balance -= TransferAmount;
            else
                cout << "Not enough money" << endl;
            break;
        }
    } while (option != 5);

    system("pause>0");
}