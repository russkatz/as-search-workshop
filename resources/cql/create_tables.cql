CREATE KEYSPACE IF NOT EXISTS ds_ins WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

create type ds_ins.contact (
		contact_id text,
                phone_home text,
                phone_cell text,
                email_address text,
                state text,
);

create TABLE IF NOT EXISTS  ds_ins.driver (
        account_id text,
        driver_id text,
        first_name text,
        last_name text,
        updated_ts timestamp,
        age_first_licensed int,
        certificate_of_financial_responsibility_required boolean,
        current_active_violations int,
        good_student_discount boolean,
        drivers_license_state text,
        driver_passed_safedriving boolean,
        good_driver_discount boolean,
        driver_resident_student boolean,
        driver_retired boolean,
        carpool_usage boolean,
        contact_info contact,
        PRIMARY KEY (account_id, driver_id)
);
CREATE SEARCH INDEX IF NOT EXISTS ON ds_ins.driver ;
COPY ds_ins.driver (account_id,driver_id,first_name,last_name,age_first_licensed,carpool_usage,certificate_of_financial_responsibility_required,current_active_violations,driver_passed_safedriving,driver_resident_student,driver_retired,drivers_license_state,good_driver_discount,good_student_discount,updated_ts,contact_info) FROM 'drivers.csv';
