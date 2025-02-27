select 
				dc.nm_cliente 
				,dc.email_ficticio
				,avg(av_servico) media_av
			from barber_shop.dw.fact_servicos_barbearia f
				join barber_shop.dw.dim_cliente dc on dc.sk_cliente = f.sk_cliente
			group by 
				dc.nm_cliente  
				,dc.email_ficticio
			order by media_av 
			limit 5