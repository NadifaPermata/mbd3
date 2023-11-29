drop table if exists selling;
create table selling (
	id serial,
	nama_petugas text,
	plat_nomor text,
	jenis_kendaraan text,
	symptom text,
	banyak_pembelian text,
	waktu time,
	tanggal date
);

insert into selling (nama_petugas, plat_nomor, jenis_kendaraan, symptom, banyak_pembelian, waktu, tanggal) 
values
	('Nuryanto', 'L 0919 CGF', 'pertamax turbo', 62838, '08:00', '2023-10-01'),
	('Angel', 'M 2348 GHT', 'pertamax', 62838, '09:00', '2022-10-02'),
	;