import psycopg2
from psycopg2.extras import DictCursor
from model.input_data import *
import time


class DbHelper:

    def __init__(self, host="localhost", dbname=None, user="postgres", password="postgres", records=None, edge_template=None, action=None):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.records = records
        self.edge_template = edge_template
        self.action = action
        self.connection = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
        self.connection.autocommit = True

    def check_cam_defocus(self, id):
        with self.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute('SELECT * FROM "OBJ_CAM_DEFOCUS" WHERE id =%s', (id,))
                self.records = cursor.fetchall()
                assert self.records != None
                assert self.records != []
                #print("records", self.records)
        cursor.close()
        return conn

    def check_cam_defocus_from_db(self, db):
        db.check_cam_defocus(id=defocusId)
        self.edge_template = db.records[0][12]
        #print(self.edge_template)


    def check_protocol_event_by_dbid(self, id):
        with self.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute('SELECT * FROM "PROTOCOL" WHERE objid =%s', (id,))
                assert self.records != []
                self.records = cursor.fetchall()
                #print("records", self.records)
        cursor.close()
        return conn

    def check_action_from_db(self, db):
        db.check_protocol_event_by_dbid()
        self.action = db.records[0][4]
        #print(self.edge_template)


    def find_focus_time(self, t2):
        with self.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                time.sleep(2)
                cursor.execute('SELECT * FROM "PROTOCOL" WHERE action =%s AND objid =%s AND time >%s', ("FOCUSED", defocusId, t2,))
                #print(t2)
                self.records = cursor.fetchall()
                assert self.records != None
                assert self.records != []
                #print("records", self.records)
        cursor.close()
        return conn

    def find_defocus_time(self):
        with self.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute('SELECT * FROM "PROTOCOL" WHERE action =%s AND objid =%s', ("DEFOCUSED", defocusId,))
                self.records = cursor.fetchall()
                assert self.records != None
                assert self.records != []
                #print("records", self.records)
        cursor.close()
        return conn

    def find_defocus_time_after_deactivation_zone(self, t3):
        with self.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute('SELECT * FROM "PROTOCOL" WHERE action =%s AND objid =%s AND time >%s', ("DEFOCUSED", defocusId, t3))
                self.records = cursor.fetchall()
                assert self.records != None
                #print("records", self.records)
        cursor.close()
        return conn

    def find_light_on(self):
        with self.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute('SELECT * FROM "PROTOCOL" WHERE action =%s AND objid =%s', ("LIGHT_ON", ld_id,))
                self.records = cursor.fetchall()
                assert self.records != None
                assert self.records != []
                print("records", self.records)
        cursor.close()
        return conn

    def find_light_off(self):
        with self.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute('SELECT * FROM "PROTOCOL" WHERE action =%s AND objid =%s', ("LIGHT_OFF", ld_id,))
                self.records = cursor.fetchall()
                assert self.records != None
                assert self.records != []
                print("records", self.records)
        cursor.close()
        return conn

    def find_shifted(self):
        with self.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute('SELECT * FROM "PROTOCOL" WHERE action =%s AND objid =%s', ("SHIFTED", tiltId,))
                self.records = cursor.fetchall()
                assert self.records != None
                assert self.records != []
                print("records", self.records)
        cursor.close()
        return conn

    def find_blinding(self):
        with self.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute('SELECT * FROM "PROTOCOL" WHERE action =%s AND objid =%s', ("BLINDING", camId,))
                self.records = cursor.fetchall()
                assert self.records != None
                assert self.records != []
                print("records", self.records)
        cursor.close()
        return conn

    def find_unblinding(self):
        with self.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute('SELECT * FROM "PROTOCOL" WHERE action =%s AND objid =%s', ("UNBLINDING", camId,))
                self.records = cursor.fetchall()
                assert self.records != None
                assert self.records != []
                print("records", self.records)
        cursor.close()
        return conn

    def find_blinding_time(self):
        with self.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute('SELECT * FROM "PROTOCOL" WHERE action =%s AND objid =%s', ("BLINDING", camId,))
                self.records = cursor.fetchall()
                assert self.records != None
                assert self.records != []
                #print("records", self.records)
        cursor.close()
        return conn

    def find_blinding_time_after_deactivation_zone(self, t3):
        with self.connection as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute('SELECT * FROM "PROTOCOL" WHERE action =%s AND objid =%s AND time >%s', ("BLINDING", camId, t3))
                self.records = cursor.fetchall()
                assert self.records != None
                #print("records", self.records)
        cursor.close()
        return conn


#cursor.execute('SELECT * FROM audit_events WHERE event_action=%s', (event_action,))
    #CONVERT_TZ(created_at, '+00:00', '+08:00')   between     "2018-01-24" and "2018-01-25"

    def clean_db(self):
        with self.connection as conn:
            with conn.cursor() as cursor:
                cursor.execute('DELETE FROM "PROTOCOL"')
                conn.commit()
        cursor.close()


    def close_connection(self):
        self.connection.close()
        print("close")




