from django.conf.urls import include, url
from .views import *
from .report import *
from empenos.apis import *

app_name="empenos"

urlpatterns=[
	#formularios
	url(r'^abrir_caja/$',abrir_caja,name="abrir_caja"),
	url(r'^otros_ingresos/$',otros_ingresos,name="otros_ingresos"),
	url(r'^retiro_efectivo/$',retiro_efectivo,name="retiro_efectivo"),
	url(r'^corte_caja/$',corte_caja,name="corte_caja"),
	url(r'^reportes_caja/$',reportes_caja,name="reportes_caja"),
	url(r'^nvo_empeno/$',nvo_empeno,name="nvo_empeno"),
	url(r'^alta_cliente/$',alta_cliente,name="alta_cliente"),
	url(r'^edita_cliente/(?P<id_cliente>\w+)/$',alta_cliente,name="edita_cliente"),
	url(r'^imprime_boleta/$',imprime_boleta,name="imprime_boleta"),
	url(r'^consulta_boleta/$',consulta_boleta,name="consulta_boleta"),
	url(r'^refrendo/(?P<id_boleta>\w+)/$',refrendo,name="refrendo"),
	url(r'^refrendo_plazo_mensual/(?P<id_boleta>\w+)/$',refrendo_plazo_mensual,name="refrendo_plazo_mensual"),
	url(r'^imprime_abono/$',imprime_abono,name="imprime_abono"),
	url(r'^re_imprimir_boleta/(?P<id_boleta>\w+)/$',re_imprimir_boleta,name="re_imprimir_boleta"),
	url(r'^re_imprimir_abono/(?P<id_abono>\w+)/$',re_imprimir_abono,name="re_imprimir_abono"),
	url(r'^rep_flujo_caja/$',rep_flujo_caja,name="rep_flujo_caja"),
	url(r'^elimina_costo_extra/$',elimina_costo_extra,name="elimina_costo_extra"),
	url(r'^admin_kilataje$',admin_kilataje,name="admin_kilataje"),
	url(r'^venta_granel$',venta_granel,name="venta_granel"),
	url(r'^imprime_venta_granel$',imprime_venta_granel,name="imprime_venta_granel"),
	url(r'^consulta_venta$',consulta_venta,name="consulta_venta"),
	url(r'^re_imprimir_venta/(?P<id_venta>\w+)/$',re_imprimir_venta,name="re_imprimir_venta"),
	url(r'^admin_porc_avaluo/$',admin_porc_avaluo,name="admin_porc_avaluo"),
	url(r'^venta_piso/$',venta_piso,name="venta_piso"),	
	url(r'^imprime_venta_piso$',imprime_venta_piso,name="imprime_venta_piso"),
	url(r'^re_imprimir_venta_piso/(?P<id_venta>\w+)/$',re_imprimir_venta_piso,name="re_imprimir_venta_piso"),
	url(r'^concepto_retiro/$',concepto_retiro,name="concepto_retiro"),
	url(r'^admin_min_apartado/(?P<id>\w+)/$',admin_min_apartado,name="admin_min_apartado"),
	url(r'^apartado/$',apartado,name="apartado"),
	url(r'^imprime_apartado$',imprime_apartado,name="imprime_apartado"),
	url(r'^consulta_apartado$',consulta_apartado,name="consulta_apartado"),
	url(r'^re_imprimir_apartado/(?P<id_apartado>\w+)/$',re_imprimir_apartado,name="re_imprimir_apartado"),
	url(r'^abona_apartado/((?P<id_apartado>\w+))/$',abona_apartado,name="abona_apartado"),
	url(r'^elimina_retiro/$',elimina_retiro,name="elimina_retiro"),
	url(r'^administracion_interes_empeno/$',administracion_interes_empeno,name="administracion_interes_empeno"),
	url(r'^administracion_porcentaje_mutuo/$',administracion_porcentaje_mutuo,name="administracion_porcentaje_mutuo"),
	url(r'^cancela_abono/$',cancela_abono,name="cancela_abono"),
	url(r'^rep_comparativo_estatus_cartera/$',rep_comparativo_estatus_cartera,name="rep_comparativo_estatus_cartera"),
	url(r'^reporte_retiros_efectivo/$',reporte_retiros_efectivo,name="reporte_retiros_efectivo"),
	url(r'^reporte_ingresos_efectivo/$',reporte_ingresos_efectivo,name="reporte_ingresos_efectivo"),
	url(r'^admin_comisionpg/$',admin_comisionpg,name="admin_comisionpg"),
	url(r'^admin_precio_venta/$',admin_precio_venta,name="admin_precio_venta"),
	url(r'^reporte_cajas_abiertas/$',reporte_cajas_abiertas,name="reporte_cajas_abiertas"),


	url(r'^imprime_comprobante_retiro/(?P<id>\w+)/$',imprime_comprobante_retiro,name="imprime_comprobante_retiro"),
	url(r'^imprime_comprobante_ingreso/(?P<id>\w+)/$',imprime_comprobante_ingreso,name="imprime_comprobante_ingreso"),
	url(r'^imprime_corte_caja/(?P<id>\w+)/$',imprime_corte_caja,name="imprime_corte_caja"),



	url(r'^consulta_abono$',consulta_abono,name="consulta_abono"),	
	url(r'^cierra_caja/$',api_cierra_caja,name="cierra_caja"),
	url(r'^envia_token/$',api_envia_token),	
	url(r'^api_consulta_corte_caja/$',api_consulta_corte_caja),	
	url(r'^re_abre_caja/$',api_re_abre_caja),
	url(r'^api_tipo_producto/$',api_tipo_producto),	
	url(r'^api_consulta_linea/$',api_consulta_linea),	
	url(r'^api_consulta_sublinea/$',api_consulta_sublinea),	
	url(r'^api_consulta_marcas/$',api_consulta_marcas),	
	url(r'^api_consulta_kilataje/$',api_consulta_kilataje),	
	url(r'^api_consulta_costo_kilataje/$',api_consulta_costo_kilataje),	
	url(r'^api_guarda_producto_temporal/$',api_guarda_producto_temporal),	
	url(r'^api_consulta_cotizacion/$',api_consulta_cotizacion),	
	url(r'^api_elimina_producto_cotizacion/$',api_elimina_producto_cotizacion),	
	url(r'^api_consulta_cliente/$',api_consulta_cliente),	
	url(r'^api_limpia_cotizacion/$',api_limpia_cotizacion),	
	url(r'^api_consulta_boleta/$',api_consulta_boleta),	
	url(r'^api_simula_refrendo/$',api_simula_refrendo),	
	url(r'^api_simula_refrendo_mensual/$',api_simula_refrendo_mensual),	
	url(r'^api_consulta_sucurales_usuario/$',api_consulta_sucurales_usuario),	
	url(r'^api_reg_costo_reimpresion/$',api_reg_costo_reimpresion),	
	url(r'^api_job_diario/$',api_job_diario),		
	url(r'^api_guarda_estatus_cartera/$',api_guarda_estatus_cartera),		
	url(r'^api_notificacion_cajas_abiertas/$',api_notificacion_cajas_abiertas,name="api_notificacion_cajas_abiertas"),
	url(r'^api_agrega_marca/$',api_agrega_marca,name="api_agrega_marca"),
	url(r'^api_elimina_costo_extra/$',api_elimina_costo_extra,name="api_elimina_costo_extra"),
	url(r'^api_elimina_costo_kilataje/$',api_elimina_costo_kilataje,name="api_elimina_costo_kilataje"),
	url(r'^api_agregar_kilataje/$',api_agregar_kilataje,name="api_agregar_kilataje"),
	url(r'^api_agrega_boleta_venta_granel/$',api_agrega_boleta_venta_granel,name="api_agrega_boleta_venta_granel"),
	url(r'^api_agrega_importe_real_venta/$',api_agrega_importe_real_venta,name="api_agrega_importe_real_venta"),
	url(r'^api_agrega_prod_venta_piso/$',api_agrega_prod_venta_piso,name="api_agrega_prod_venta_piso"),
	url(r'^api_consulta_prod_temporal_piso/$',api_consulta_prod_temporal_piso,name="api_consulta_prod_temporal_piso"),
	url(r'^api_elimina_prod_venta_piso/$',api_elimina_prod_venta_piso,name="api_elimina_prod_venta_piso"),
	url(r'^api_limpia_venta_piso/$',api_limpia_venta_piso,name="api_limpia_venta_piso"),
	url(r'^api_consulta_cliente_2/$',api_consulta_cliente_2,name="api_consulta_cliente_2"),
	url(r'^api_agrega_prod_apartado/$',api_agrega_prod_apartado,name="api_agrega_prod_apartado"),
	url(r'^api_consulta_prod_temporal_apartado/$',api_consulta_prod_temporal_apartado,name="api_consulta_prod_temporal_apartado"),
	url(r'^api_elimina_prod_apartado/$',api_elimina_prod_apartado,name="api_elimina_prod_apartado"),
	url(r'^api_concepto_retiro/$',api_concepto_retiro,name="api_concepto_retiro"),
	url(r'^api_valida_importe_retiro/$',api_valida_importe_retiro,name="api_valida_importe_retiro"),
	url(r'^api_cancela_retiro/$',api_cancela_retiro,name="api_cancela_retiro"),
	url(r'^api_consulta_configuracion_empeno/$',api_consulta_configuracion_empeno,name="api_consulta_configuracion_empeno"),
	url(r'^api_porcentaje_mutuo/$',api_porcentaje_mutuo,name="api_porcentaje_mutuo"),
	url(r'^api_cliente/$',api_cliente,name="api_cliente"),
	url(r'^api_backup/$',api_backup,name="api_backup"),
	url(r'^api_simula_proximos_pagos_semanal/$',api_simula_proximos_pagos_semanal,name="api_simula_proximos_pagos_semanal"),
	url(r'^api_aplica_refrendo_semanal/$',api_aplica_refrendo_semanal,name="api_aplica_refrendo_semanal"),
	url(r'^api_cancela_abono/$',api_cancela_abono,name="api_cancela_abono"),
	url(r'^api_kiltajes/$',api_kiltajes,name="api_kiltajes"),
	url(r'^api_precio_venta_fijo/$',api_precio_venta_fijo,name="api_precio_venta_fijo"),




]
