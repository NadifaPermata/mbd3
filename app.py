import streamlit as st
from sqlalchemy import text

list_petugas = ['', 'Nuryanto', 'Angel', 'Siola', 'Riki', 'Karan']
list_symptom = ['', 'pertalite', 'pertamax', 'pertamax turbo', 'solar', 'pertamina dex']

conn = st.connection("postgresql", type="sql", 
                     url="postgresql://NadifaPermata:7CIXwskWNRy0@ep-falling-cherry-06864175.us-east-2.aws.neon.tech/web")
with conn.session as session:
    query = text('CREATE TABLE IF NOT EXISTS SELLING (id serial, nama_petugas varchar, plat_nomor char(25), jenis_kendaraan varchar, \
                                                       symptom text, banyak_pembelian varchar, tanggal date);')
    session.execute(query)

st.header('SPBU DATA MANAGEMENT')
page = st.sidebar.selectbox("Pilih Menu", ["View Data","Edit Data"])

if page == "View Data":
    data = conn.query('SELECT * FROM selling ORDER By id;', ttl="0").set_index('id')
    st.dataframe(data)

if page == "Edit Data":
    if st.button('Tambah Data'):
        with conn.session as session:
            query = text('INSERT INTO selling (nama_petugas, plat_nomor, jenis_kendaraan, symptom, banyak_pembelian, waktu, tanggal) \
                          VALUES (:1, :2, :3, :4, :5, :6, :7, :8);')
            session.execute(query, {'1':'', '2':'', '3':'', '4':'[]', '5':'', '6':'', '7':None, '8':None})
            session.commit()

    data = conn.query('SELECT * FROM selling ORDER By id;', ttl="0")
    for _, result in data.iterrows():        
        id = result['id']
        nama_petugas_lama = result["nama_petugas"]
        plat_nomor_lama = result["plat_nomor"]
        symptom_lama = result["symptom"]
        banyak_pembelianlama = result["handphone"]
        address_lama = result["address"]
        waktu_lama = result["waktu"]
        tanggal_lama = result["tanggal"]

        with st.expander(f'a.n. {patient_name_lama}'):
            with st.form(f'data-{id}'):
                doctor_name_baru = st.selectbox("doctor_name", list_doctor, list_doctor.index(doctor_name_lama))
                patient_name_baru = st.text_input("patient_name", patient_name_lama)
                gender_baru = st.selectbox("gender", list_symptom, list_symptom.index(gender_lama))
                symptom_baru = st.multiselect("symptom", ['cough', 'flu', 'headache', 'stomache'], eval(symptom_lama))
                handphone_baru = st.text_input("handphone", handphone_lama)
                address_baru = st.text_input("address", address_lama)
                waktu_baru = st.time_input("waktu", waktu_lama)
                tanggal_baru = st.date_input("tanggal", tanggal_lama)
                
                col1, col2 = st.columns([1, 6])

                with col1:
                    if st.form_submit_button('UPDATE'):
                        with conn.session as session:
                            query = text('UPDATE schedule \
                                          SET doctor_name=:1, patient_name=:2, gender=:3, symptom=:4, \
                                          handphone=:5, address=:6, waktu=:7, tanggal=:8 \
                                          WHERE id=:9;')
                            session.execute(query, {'1':doctor_name_baru, '2':patient_name_baru, '3':gender_baru, '4':str(symptom_baru), 
                                                    '5':handphone_baru, '6':address_baru, '7':waktu_baru, '8':tanggal_baru, '9':id})
                            session.commit()
                            st.experimental_rerun()
                
                with col2:
                    if st.form_submit_button('DELETE'):
                        query = text(f'DELETE FROM schedule WHERE id=:1;')
                        session.execute(query, {'1':id})
                        session.commit()
                        st.experimental_rerun()