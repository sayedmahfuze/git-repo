--# Example 10-2 Passing Associative Array to Standalone Subprogram 

CREATE OR REPLACE PACKAGE aa_pkg AUTHID DEFINER AS 
    TYPE aa_type IS TABLE OF INTEGER INDEX BY VARCHAR2(15);
END aa_pkg;
/


CREATE OR REPLACE PROCEDURE print_aa(
    aa aa_pkg.aa_type
) AUTHID DEFINER IS 
    i VARCHAR2(15);
BEGIN 
    i := aa.FIRST;
    
    WHILE i IS NOT NULL LOOP 
        DBMS_OUTPUT.PUT_LINE(aa(i) || ' ' || i);
        i := aa.NEXT(i);
    END LOOP;
END;
/

DECLARE 
    aa_var  aa_pkg.aa_type;
BEGIN 
    aa_var('zero')  := 0;
    aa_var('one')   := 1;
    aa_var('two')   := 2;
    
    print_aa(aa_var);
END;
/

        