import sqlite3 as sql

## Comienzo del proyecto de Finanzas  
print("Con esto comienza el proyecto")

Base = sql.connect('base_principal.db')

cursor = Base.cursor()

#Creación de Entidades de la BD
cursor.execute("PRAGMA foreign_keys = ON;")

#Borrado de tablas
cursor.execute("DROP TABLE IF EXISTS Flujo;")
cursor.execute("DROP TABLE IF EXISTS Transacciones;")
cursor.execute("DROP TABLE IF EXISTS Info_transacciones;")
cursor.execute("DROP TABLE IF EXISTS Rubro;")
cursor.execute("DROP TABLE IF EXISTS Anual;")
cursor.execute("DROP TABLE IF EXISTS Mensual;")
cursor.execute("DROP TABLE IF EXISTS Semanal;")
cursor.execute("DROP TABLE IF EXISTS Diario;")

#Creación de las tablas
cursor.execute(""" 
               CREATE TABLE Diario(
                        DIA_ID      integer NOT NULL
                        ,FECHA      date    NOT NULL
                        ,DIA_SALDO  numeric
                        ,SALDO      numeric
                        ,PROMEDIO   numeric
                        ,MEDIANA    numeric
                        ,MODA       numeric
                        ,CONSTRAINT D_ID_PK PRIMARY KEY (DIA_ID AUTOINCREMENT)
                    );
""") 
cursor.execute("""
                CREATE TABLE Semanal(
                        SEMANA_ID       integer NOT NULL
                        ,SEMANA_INICIO  date    NOT NULL
                        ,SEMANA_FIN     date    NOT NULL
                        ,SEMANA_SALDO   numeric NOT NULL
                        ,SALDO          numeric NOT NULL
                        ,PROMEDIO       numeric NOT NULL
                        ,MEDIANA        numeric NOT NULL
                        ,MODA           numeric NOT NULL
                        ,CONSTRAINT S_ID_PK PRIMARY KEY (SEMANA_ID AUTOINCREMENT)
                        ,CONSTRAINT SEM_DIA_INI_FK FOREIGN KEY (SEMANA_INICIO) REFERENCES Diario (DIA_ID)
                    	,CONSTRAINT SEM_DIA_FIN_FK FOREIGN KEY (SEMANA_FIN)    REFERENCES Diario (DIA_ID)
                    );
""") 

cursor.execute("""
                CREATE TABLE Mensual(
                        MES_ID          integer NOT NULL
                        ,MES_INICIO     date    NOT NULL
                        ,MES_FIN        date    NOT NULL
                        ,MES_SALDO      numeric NOT NULL
                        ,SALDO          numeric NOT NULL
                        ,PROMEDIO       numeric NOT NULL 
                        ,MEDIANA        numeric NOT NULL 
                        ,MODA           numeric NOT NULL
                        ,CONSTRAINT M_ID_PK PRIMARY KEY (MES_ID AUTOINCREMENT)
                        ,CONSTRAINT MES_DIA_INI_FK FOREIGN KEY (MES_INICIO)   REFERENCES Diario (DIA_ID)
                        ,CONSTRAINT MES_DIA_FIN_FK FOREIGN KEY (MES_FIN)      REFERENCES Diario (DIA_ID)
                    );
""")  

cursor.execute("""
                CREATE TABLE Anual(
                        ANIO_ID         integer NOT NULL
                        ,ANIO_INICIO    date    NOT NULL
                        ,ANIO_FIN       date    NOT NULL
                        ,ANIO_SALDO     numeric NOT NULL 
                        ,SALDO          numeric NOT NULL
                        ,PROMEDIO       numeric NOT NULL
                        ,MEDIANA        numeric NOT NULL
                        ,MODA           numeric NOT NULL
                        ,CONSTRAINT A_ID_PK PRIMARY KEY (ANIO_ID AUTOINCREMENT)
                        ,CONSTRAINT ANUAL_MES_INI_FK FOREIGN KEY (ANIO_INICIO)   REFERENCES Mensual (MES_INICIO)
                        ,CONSTRAINT ANUAL_MES_FIN_FK FOREIGN KEY (ANIO_FIN)      REFERENCES Mensual (MES_FIN)
                    );
""") 

cursor.execute("""
                CREATE TABLE Rubro(
                        RUBRO_ID    integer NOT NULL
                        ,TIPO       text    NOT NULL
                        ,CONSTRAINT RUBRO_ID_PK PRIMARY KEY (RUBRO_ID AUTOINCREMENT)
                        );
""") 

cursor.execute("""
                CREATE TABLE Info_transacciones(
                        INFO_ID     integer  NOT NULL
                        ,COCEPTO    date     NOT NULL
                        ,CANTIDAD   numeric  NOT NULL
                        ,RUBRO_ID   integer
                        ,CONSTRAINT I_ID_IT_PK PRIMARY KEY(INFO_ID AUTOINCREMENT)
                        ,CONSTRAINT INFO_RUBRO_R_ID_FK FOREIGN KEY (RUBRO_ID) REFERENCES Rubro (RUBRO_ID)
                    );
""")                  
cursor.execute("""
                CREATE TABLE Transacciones(
                        TRANSACCION_ID      integer  NOT NULL
                        ,FECHA              datetime NOT NULL
                        ,INFO_ID            integer  NOT NULL
                        ,DIA_ID             integer  NOT NULL
                        ,CONSTRAINT T_D_T_PK PRIMARY KEY(TRANSACCION_ID AUTOINCREMENT)
                        ,CONSTRAINT TRANSAC_INFO_ID_FK FOREIGN KEY (INFO_ID)   REFERENCES Info_transacciones (INFO_ID)
                        ,CONSTRAINT TRANSAC_DIA_ID_FK  FOREIGN KEY (DIA_ID)    REFERENCES Diario (DIA_ID)
                    );
""") 


cursor.execute("""
            CREATE TABLE Flujo(
                        OPERACION_ID    integer NOT NULL
                        ,TRANSACCION_ID integer NOT NULL
                        ,INTERVALO      numeric
                        ,INTERESES      numeric
                        ,CONSTRAINT O_ID_PK PRIMARY KEY(OPERACION_ID,TRANSACCION_ID)
                        ,CONSTRAINT FLUJ_TRANS_ID_FK FOREIGN KEY (TRANSACCION_ID)   REFERENCES Transacciones (TRANSACCION_ID)  
                    );
""")



Base.commit()

cursor.close()
Base.close()