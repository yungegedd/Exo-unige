#include <math.h>
#include <stdio.h>


void exercice1(void){
    printf("\n\nEXERCICE 1\n\n");
    
    printf("Bonjour monde !\n");
    
    return;
}


void exercice2(void){
    printf("\n\nEXERCICE 2\n\n");
    
    /******************** Votre code ci-dessous ********************/
    printf("Nom     : Glory DANIGUE");
    printf("Né le   :10.08.2006");
    printf("Contact :glorydanigue423@gmail.com");

    /******************** Votre code ci-dessus *********************/
    
    return;
}


void exercice3(void) {
    printf("\n\nEXERCICE 3\n\n");
    
    /******************** Votre code ci-dessous ********************/
    printf("     #   ");
    printf("  #     #");
    printf("#       #");
    printf("#       #");
    printf("#       #");
    printf(" #      #");
    printf("  #     #");
    printf("#########");
    printf("#########");
    
    
    

    /******************** Votre code ci-dessus *********************/

    return;
}


void exercice4(void) {
    printf("\n\nEXERCICE 4\n\n");

    /******************** Votre code ci-dessous ********************/
    char c1='U';
    char c2='N';
    char c3='I';
    char c4='G';
    char c5='E';

    printf("%c%C%C%C%C",c1,c2,c3,c4,c5);
    /******************** Votre code ci-dessus *********************/
    
    return;
}


void exercice5(void) {
    printf("\n\nEXERCICE 5\n\n");

    const float PI = 3.1415926535;

    // Lecture du rayon
    float radius;
    printf("Entrer le rayon du cercle (en m) : ");
    scanf("%f", &radius);

    /******************** Votre code ci-dessous ********************/
    float perimètre;
    printf("Le perimetre du cercle est :%f",2*radius*PI);
    /******************** Votre code ci-dessus *********************/

    return;
}


void exercice6(void) {
    printf("\n\nEXERCICE 6\n\n");

    // Lecture de la date de naissance
    int birth_year, birth_month, birth_day;
    printf("Entrer votre date de naissance (format dd/mm/yyyy) : ");
    scanf("%d/%d/%d", &birth_day, &birth_month, &birth_year);

    // Lecture de la date du jour
    int today_year, today_month, today_day;
    printf("Entrer la date d'aujourd'hui (format dd/mm/yyyy) : ");
    scanf("%d/%d/%d", &today_day, &today_month, &today_year);

    // Affiche les dates entrées par l'utilisateur
    printf("Je suis né.e le %d/%d/%d.\n", birth_day, birth_month, birth_year);
    printf("Aujourd'hui, nous sommes le %d/%d/%d.\n\n", today_day, today_month, today_year);    

    int age_in_day = 0;

    /******************** Votre code ci-dessous ********************/
    age_in_day=today_year*360+today_month*30+today_day;

    /******************** Votre code ci-dessus *********************/

    printf("==> Mon âge est (approximativement) de %d jours.\n", age_in_day);
    
    return;
}


void exercice7(void) {
    printf("\n\nEXERCICE 7\n\n");

    // Lecture du nombre de jours
    int nb_of_days;
    printf("Entrer un nombre de jours à convertir : ");
    scanf("%d", &nb_of_days);
    int nb_of_month;
    int nb_of_year;
    int nb_of_week;
   
    /******************** Votre code ci-dessous ********************/
    nb_of_year=nb_of_days/360;
    nb_of_month=(nb_of_days%360)/30;
    nb_of_week=nb_of_month*4;
    nb_of_days=(nb_of_days%360)%30;

    printf("%d jours font %d années,%d mois,%d semaines et %d jours",nb_of_days,nb_of_year,nb_of_month,nb_of_week,nb_of_days);

    /******************** Votre code ci-dessus *********************/

    return;
}


void exercice8(void) {
    printf("\n\nEXERCICE 8\n\n");

    int a = 7, b = 2;
    float c;  
    
    /******************** Votre code ci-dessous ********************/
    c= (float) a/b;
    /******************** Votre code ci-dessus *********************/
    
    printf("%d / %d = %f \n", a, b, c);

    return;
}


void exercice9(void) {
    printf("\n\nEXERCICE 9\n\n");
    
    /**************************************************************/
    /********* Exemple d'overflow du type 'unsigned char' *********/
    /**************************************************************/

    unsigned char a, b, c;

    // Vérifions qu'un 'unsigned char' occupe bien 8 bits
    int size_of_unsigned_char = sizeof(a);
    printf("Le type 'unsigned char' utilise %d octets, c'est-à-dire %d bits.\n", size_of_unsigned_char, 8 * size_of_unsigned_char);

    // Exemple d'overflow
    a = 61;
    b = 213;
    c = a + b;  // Overflow : c ne vaut pas 61 + 213 = 274 mais 274 % 256 = 18
    printf("%d + %d = %d\n", a, b, c);
    
    /*************************************/
    /********* Fin de l'exemple *********/
    /*************************************/


    /******************** Votre code ci-dessous ********************/

    /******************** Votre code ci-dessus *********************/

    return;
}


int main(void) {   

    // Astuce : commenter tous les exercices sauf celui en cours pour gagner du temps !

    exercice1();
    exercice2();
    exercice3();
    exercice4();
    exercice5();    
    exercice6();
    exercice7();
    exercice8();
    //exercice9();

    return 0;
}