# -*- coding: utf-8 -*-

from openerp.osv import fields, osv


class Gastos_Mensuales(osv.osv):
	_name = 'gastos.mensuales'
	_columns = {
		'_estado': fields.char('Estado', required=True,),
		'jefe_estado': fields.char('Jefe de Estado', required=True,),
		'_responsable': fields.char('Responsable', required=True,),
		'cargar_fecha': fields.datetime('Fecha de carga',),
		'partida': fields.char('Partida',),
		'denominacion': fields.char('Denominacion',),
		'rubro': fields.char('Rubro',),
		'cantidad': fields.integer('Cantidad',),
		'precio': fields.float('Precio',),
		'is_done': fields.boolean('Done?'),
	}

class Gastos_Nomina(osv.osv):
	_name = 'gastos.nomina'
	_columns = {
		'cargo': fields.selection([('Jubilado','Jubilado'),('Obrero','Obrero'),('Bachiller','Bachiller'),('Bachiller II','Bachiller II'),('Bachiller III','Bachiller III'),('Técnico','Técnico'),('Técnico II','Técnico II'),('Profesional','Profesional'),('Profesional II','Profesional II'),('Profesional III','Profesional III'),('Líder de Área 13%','Líder de Área 13%'),('Líder de Área 15%','Líder de Área 15%'),('Líder de Área 17%','Líder de Área 17%'),('Líder de Área','Líder de Área'),('Coordinador','Coordinador'),('Jefe de Oficina de Estado','Jefe de Oficina de Estado'),('Jefe de Divición','Jefe de Divición'),('Gerente','Gerente'),('Gerente General','Gerente General'),('Presidente','Presidente')],'Cargo', help="Selecciones el cargo que ocupa el trabajador en la Institución"),
		'cantidad': fields.integer('Cantidad', help="Indique la cantidad de trabajadores en el mismo cargo"),
		'monto': fields.float('Monto',),	
	}