#include <stdio.h>
#include <stdlib.h>
#include <string.h>

unsigned long jump_offset;

int intro(void){
    puts(">>> ALERT: CRITICAL SYSTEM FAILURE >>>");
    puts("Core containment sealed. Autonomous protocols are counting down.");
    puts("Only a manually supplied override key can halt the shutdown sequence.");
    puts("Submit the key now. The clock is not your friend.\n");
    return 0;
}

int win(void){
    puts("*** OVERRIDE ACCEPTED. DETONATION ABORTED ***");
    puts("You stopped it in time. Here's the recovery key:");
    FILE *fd = fopen("flag.txt", "r");
    char buf[128];
    fgets(buf, sizeof(buf), fd);
    printf("%s\n", buf);
    fclose(fd);
    fflush(stdout);
    exit(0);

    return 0;
}

int main(void){
    intro();


    printf("main at:  %p\n", (void*)main);

    printf("\nEnter override offset in hex relative to main ");
    if (scanf("%lx", &jump_offset) != 1) {
        puts("failed to read override offset");
        return 1;
    }

    unsigned long target = (unsigned long) main + jump_offset;


    if (target == (unsigned long)win) {

        void (*fptr)(void) = (void(*)(void))target;
        fptr();
    } else {
        puts("Override rejected: invalid offset.");

    }

    return 0;
}
