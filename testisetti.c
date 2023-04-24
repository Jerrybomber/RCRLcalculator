/*
File:		Calculator.c
Author:		Jerry Karkainen
Description:C code calculating rc and rl circuit, input from python.
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define PI 3.14159265358979323846

//Structs for circuits.
struct RCCircuit {
	float xc;
	float current;
    float z;
    float uc;
    float ur;
};

struct RLCircuit {
	float xl;
	float current;
    float z;
    float ul;
    float ur;
};

//Creating memory space for structs
struct RLCircuit* createRLCircuit(int step) {
    struct RLCircuit *pointer = NULL;
    
   	pointer = (struct RLCircuit *) malloc(step * sizeof(struct RLCircuit));
    
    if (pointer == NULL) {
        printf("Memory allocation failed\n"); // Check if memory allocation fails
        return NULL;
    }
    
    return pointer;
}

struct RCCircuit* createRCCircuit(int step) {

    struct RCCircuit *pointer = NULL;
    
    pointer = (struct RCCircuit *) malloc(step * sizeof(struct RCCircuit));
    
    if (pointer == NULL) {
        printf("Memory allocation failed\n");
        return NULL;
    }
    return pointer;
}

//Calculating values and addint them in structs.
void addRLvalues(int v, int r, int l, int fStart, int step, int fStep, struct RLCircuit *pointer) {
	for (int i = 0; i < step; i++) {
    	float xl = 2 * PI * fStart * l * 0.001;
    	(pointer + i)->xl = xl;
    	float z = sqrt(pow(r, 2) + pow(xl, 2));
    	(pointer + i)->z = z;
    	float current = v / z * 1000;
    	(pointer + i)->current = current;
    	float ur = r * current * 0.001;
    	(pointer + i)->ur = ur;
    	float ul = xl * current * 0.001;
    	(pointer + i)->ul = ul;
    	fStart += fStep;
    	
    }
}

void addRCvalues(int v, int r, int c, int fStart, int step, int fStep, struct RCCircuit *pointer) {
	for (int i = 0; i < step; i++) {
    	float xc =1 / (2 * PI * fStart * c * 0.000001);
    	(pointer + i)->xc = xc;
    	float z = sqrt(pow(r, 2) + pow(xc, 2));
    	(pointer + i)->z = z;
    	float current = v / z * 1000;
    	(pointer + i)->current = current;
    	float ur = r * current * 0.001;
    	(pointer + i)->ur = ur;
    	float uc = xc * current * 0.001;
    	(pointer + i)->uc = uc;
    	fStart += fStep;
    }
}

//writing results to the text file.
void writeRCresultsToFile(struct RCCircuit *pointer, int step, int fStart, int fStep) {
	
	//Clears the textfile
	fopen("Results.txt","w");
	
	FILE *filePointer = NULL;
	
	filePointer = fopen("Results.txt","a");
	
	if (filePointer == NULL) {
		printf("Error, could not open the file\n");
		exit(1);
	}

	for (int i = 0; i < step; i++) {
		fprintf(filePointer, "hz:%d, xc:%.2f, z:%.2f, a:%.2f, uc:%.2f, ur:%.2f\n",
		fStart,
		(pointer + i)->xc,
		(pointer + i)->z,
		(pointer + i)->current,
		(pointer + i)->uc,
		(pointer + i)->ur);
		fStart += fStep;
	}
	
	fclose(filePointer);
	
}

void writeRLresultsToFile(struct RLCircuit *pointer, int step, int fStart, int fStep) {
	
	//Clears the textfile
	fopen("Results.txt","w");
	
	FILE *filePointer = NULL;
	
	filePointer = fopen("Results.txt","a");
	
	if (filePointer == NULL) {
		printf("Error, could not open the file\n");
		exit(1);
	}

	for (int i = 0; i < step; i++) {
		fprintf(filePointer, "hz:%d, xl:%.2f, z:%.2f, a:%.2f, ul:%.2f, ur:%.2f\n",
		fStart,
		(pointer + i)->xl,
		(pointer + i)->z,
		(pointer + i)->current,
		(pointer + i)->ul,
		(pointer + i)->ur);
		fStart += fStep;
	}
	
	fclose(filePointer);
	
}

//run code called from python
void runRC(int v, int r, int c, int fStart, int fStep, int fMax){
	
	int tempf = fStart;
	int step = 0;
	
	while (tempf <= fMax) {
		step += 1;
		tempf += fStep;
	}
	
	struct RCCircuit *pointer = createRCCircuit(step);
	
	addRCvalues(v, r, c, fStart, step, fStep, pointer);
	writeRCresultsToFile(pointer, step, fStart, fStep);
        
	free(pointer);   
	
}

void runRL(int v, int r, int l, int fStart, int fStep, int fMax){
	
	int tempf = fStart;
	int step = 0;


	while (tempf <= fMax) {
		step += 1;
		tempf += fStep;
	}
	
	struct RLCircuit *pointer = createRLCircuit(step);
	
	addRLvalues(v, r, l, fStart, step, fStep, pointer);
	writeRLresultsToFile(pointer, step, fStart, fStep);
        
	free(pointer);   
	
}
	

				
