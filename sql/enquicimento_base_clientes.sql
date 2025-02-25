alter table barber_shop.dw.dim_cliente add cpf_ficticio varchar;
alter table barber_shop.dw.dim_cliente add celular_ficticio varchar;
alter table barber_shop.dw.dim_cliente add email_ficticio varchar;
alter table barber_shop.dw.dim_cliente add instagram_ficticio varchar;

update barber_shop.dw.dim_cliente
	set 
		cpf_ficticio = lpad(floor(random() * 999)::text, 3, '0') || '.' ||
    lpad(floor(random() * 999)::text, 3, '0') || '.' ||
    lpad(floor(random() * 999)::text, 3, '0') || '-' ||
    lpad(floor(random() * 99)::text, 2, '0')
		,celular_ficticio = '(' || floor(random() * 90 + 10)::int || ') 9' || 
    floor(random() * 10000)::int || '-' || 
    floor(random() * 10000)::int
		,email_ficticio = concat(lower(split_part(nm_cliente,' ',1)),'.',lower(split_part(nm_cliente,' ',2)),'@fakemail.com')
		,instagram_ficticio = concat('@',lower(split_part(nm_cliente,' ',1)),'.',lower(split_part(nm_cliente,' ',2)))

	
	
	select *from barber_shop.dw.dim_cliente

