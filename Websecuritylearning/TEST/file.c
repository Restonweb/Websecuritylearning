#include <stdio.h>
#include <stdlib.h>

void readSpecificLine(FILE *file, int lineNumber) {
    char buffer[512];  
    fseek(file, 0, SEEK_SET);

    for (int i = 1; i < lineNumber; ++i) {
        if (fgets(buffer, sizeof(buffer), file) == NULL) {
            printf("Error: Line %d not found.\n", lineNumber);
            return;
        }
    }

    if (fgets(buffer, sizeof(buffer), file) != NULL) {
        printf("Line %d: %s", lineNumber, buffer);
    } else {
        printf("Error: Line %d not found.\n", lineNumber);
    }
}

void readBinaryFile(FILE *file) {
    char buffer[512];
    size_t bytesRead;

    fseek(file, 0, SEEK_SET);

    while ((bytesRead = fread(buffer, 1, sizeof(buffer), file)) > 0) {
        for (size_t i = 0; i < bytesRead; ++i) {
            printf("%02X ", buffer[i]);  
        }
    }

    printf("\n");
}

int main() {
    char fileName[100];
    int lineNumber;

    printf("Enter the file name: ");
    scanf("%s", fileName);

    FILE *file = fopen(fileName, "r");

    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    printf("Enter the line number to read: ");
    scanf("%d", &lineNumber);

    readSpecificLine(file, lineNumber);

    printf("\nBinary representation of the file:\n");
    readBinaryFile(file);

    fclose(file);

    return 0;
}
