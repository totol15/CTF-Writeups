#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define COUNTDOWN_SIZE 8
#define ABORT_CODE_SIZE 8


char countdown[COUNTDOWN_SIZE] = "T-minus";
char abort_code[ABORT_CODE_SIZE] = "SAFE";

int intro(){
    puts("DOOMSDAY SEQUENCE ENGAGED");
    puts("Reactor core sealed. Override authorization required to prevent detonation.\n");

    puts("  /\\     |\\**/|      ");
    puts(" /  \\    \\ == /       ");
    puts(" |  |     |  |        ");
    puts(" |  |     |  |        ");
    puts("/ == \\    \\  /        ");
    puts("|/**\\|     \\/         ");
    puts("\nEnter override key to initiate manual abort sequence.\n");

    return 0;
}



int accept_input(void){
    printf("Enter override payload: ");
    scanf("%s", countdown);
    return 0;
}

int check_override(){
    if (strcmp(abort_code, "SAFE") != 0){
        puts("\n*** OVERRIDE ACCEPTED. DETONATION ABORTED ***");
        FILE *fd = fopen("flag.txt", "r");
        if (!fd){
            puts("[!] flag.txt not found. Few seconds too late?");
            exit(1);
        }
        char buf[128];
        fgets(buf, sizeof(buf), fd);
        printf("%s\n", buf);
        fclose(fd);
        fflush(stdout);
        exit(0);
    } else {
        puts("\nOverride failed. Reactor still locked.");
        puts("Try overflowing the countdown buffer to flip the abort code...");
    }
    return 0;
}

int main(void){
    intro();

    accept_input();


    check_override();

    return 0;
}
