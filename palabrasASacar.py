stopwords_common = ['vacuna', 'covid', 'coronavirus', 'v', 'om','rusa', 'china', 'sputnik', 'sputnikv', 'si', 'q', 'ahora', 'vacunas', 'país', 'ser', 'salud', '3','va', 'solo', 'van', 'años', '2', 'mayores', 'primer', 'así', 'mundo', 'dice','gente', 'través', 'hace', '60', 'menos', 'puede', 'hoy', 'primera', 'después', 'bien', 'dijo',  'países', 'mil', '000', 'mejor', 'uso', 'rt', 'primero', 'ver', 'según', 'personas', 'quieren', 'poner', 'mas', 'dos',  'segunda', 
'hacer','sirve', 'días',  'tan', '1', 'aprobada', 'd', 'quiere', 'compra', 'vía', 'vacunación', 'dicen', 'cómo', 'nadie', 'decir', 'da', '100', 'llega', 'the',  'sabe', 'tener', 'mismo', '10', 'bueno', 'información', 
'datos', 'aún',  'creo', 'ningún', 'buena', 'gracias', 'aquí', 'parece', 'día', 'x', 'todas', 'quiero', 'vez', '5', 'pueblo', 'debe', 'verdad', 'и', 'población', 'dar', 'probar', 'recibir', 'podría', 'semana', '50', 'mientras', 'mal', 'cuenta', 'igual','parte', 'acá', 'año', 'vamos', '91', 'pongan', 'viene', 'ninguna', 'meses', 'seguridad',  'voy', 'pues', 'ponerse', 'diciembre', '20', 'sólo', 'europea','6', 'recibe', 'falta', 'pueden', 'sido', 'vos',  'llegó', 'cada', 'aplicar', 'astrazeneca', 'luego', 'vacunarse', 'tras', 'ministro', 'fin', 'siempre', 'prueba', '4', 'llegada', 'ue', 'toda', 'favor', 'primeros', 'entonces', 'lista', 'primeras', 'nacional', 'momento', 'tiempo', 'internacional', 'seguro', 'noticia', '92', 'gran', 'además', 'vacunado', 
'proceso', 'voluntario', 'saber', 'funciona', 'dudas', 'traer', 'cosas', 'ustedes', 'usted', 'nueva', 'claro', 'personal', 'tema', 'recibió', 'hizo', 'peor','mañana', 'moderna', 'misma', 'pasa', 'vida', 'revista', 'aplicarse', 'iii', 'usa', 'científica', 'hacen', 'haciendo', 'espera', 'pongo', 'aplicación', 'puse', 'nuevo', 'nunca', 'dan', 'hecho', 'todavía', 'alguien', 'problema', '25', 'sino', 'puso', 'haber', 'ahí', 'centro', 'tal',  'paso', '2021', 'producir', 'mala', 'caso', 'via', 'probada', 'cierto', 'tercera', 'cualquier', 'internacionales', 'я', 
'mes', 'dr',  'usar', 'médico', 'tampoco', 'espero', 'creen', 'enero', 'esperar', 'epivaccorona', 'fda', 'política', 'cosa', 'aprueba', 'k', 'aunque', 'poder', 'tres', 'mayor', 'dio', 'video', 'vladimir', 'llegará', '300', 'sigue', 'ayer', 'comienza', 'aprobó', 'detalles', 'llegue', 'ponen', 'mx', 'habla', 'adultos', 'buenos', 'medio', 'dólares', 'pais', 'informó', 'pusieron', 'cargamento', 'estan', 'ojalá', 'diciendo', 'sé', 'casi', 'hospital', 
'cara', 'contrato', 'llegar', 'autorización', 'mundial', 'posible', 'unión', 'hicieron', 'final', 'saben', 'ejemplo', 'confiable', 'llegan', 'latina', 'vas', 'pasado', 'duda', 'laboratorios', 'millón', 'amlo', 'nota', 'muestra', 'pone', 'cofepris', 'jajaja', 'nicolás', 'agencia', 'forma', 'hablar', '12', 'mira', 'sale', 'genera', 'total', 'pregunta', 'efectoski', 'dios', 'recibieron', '95', 'llegaron', 'quién', 'amigos', 'tomar', 'razón', 'esperando', 'adquirir', '2020', 'secundarioski', 'grupo', 'xq', 'anti', 'aprobar', 'puesto', 'ojo', 'demás', 'respecto', 'pondría', 'asi', 'régimen',  'recibirá', 'dieron', 'desarrollo', 'investigación', 'científico', 'fondo', 'vacunen', 'etc', 'siendo', 'cuál', 'frente', 'octubre', 'salir', '500', '24', 'nivel', 'cansino', 'compraron', 'varios', 'ir', 'importa', 'ponerme', 'sabemos', 'protección', 'compró', 'deben', 'ponga', 'hablando', 'cuento', 'encima', 'problemas', 'entiendo', 'unidos', 'vacunaron', 'ciencia', 'pasó', 'segundo', 'tipo', 
'digo', 'humanos', 'pronto', 'llegarán', 'nombre', 'guerra', 'dicho', 'único', 'sola', 'gt', 'debería', 'mismos', 'autoriza',  'autoridades', 'vacuno', 'gratis', 'marzo',  'asegura', 'лопес', 'vacunando', 'prefiero', 'importante', 'mentira', 'única', 'resto', 'deja', '90', 'informe', 'firma', 'mucha', 'lunes', 'aplicó', 'barata', 'dijeron', 'febrero', '8', 'seguir', 'llama', 'bajo', 'oposición', 'comprará', 'siquiera', 'médica', 'veo', 'venga', 'derecho', 'miles', 'salió', 'comenzará', 'twitter', 'buen', '18feb', '30', 'ah', 'lado', 'expertos', 'agua', 'alguna', 'creadores', 'aplica', 'ofrece', '200', 'hola', 'etapa', 'autorizó', 'muchas', 'cree', 'dejen', 'sos', 'algún', 'periodista', 'siguen', 'anuncio', 'serio', 'queremos', 'buenas', 'leer', 'existe', 
'necesita', 'hora', '7', 'ud', 'señor', 'vuelo', 'opinión', 'dónde', 'manera', 'puedo', 'registro', 'última', 've', 'c', 'президент', 'ema', 'confirmó', 'podrá', 'persona', 'medicamentos', '15', 'creer', 'u', 'atención', 'cuanto', 'realidad', 'pide', 'queda', 'éxito', 'grandes', 'decían', 'masiva', 'participantes', 'ayuso', 'empezar', 'baja', 'iba', 'semanas', 'convierte', 'trae', 'inicia', 'обрадор', 'veces', 'jajajaja', 'próxima', 'publica', '40', 'normal', 'resulta', 'vacunó', 'pedo', 'adquisición', 'pensar', 'aseguró', 'comunidad', 'partir', 'pasar', 'empresa', 'jueves', 'allá', 'prensa', 'aplicará', 'madre', 'porqué', 'mercado',  'autorizada', '70', 'publicado', 'vaya', 'lugar', 'alta', 'familia', 'visto', 'dinero', 'haga', 'desarrollaron', 'pa', 'hijo', 'cuándo', '11', 's', 'cambio', '42', 'cadena', 'agosto', 'oficial', 'aun', 'análisis', 'noviembre', 'disponible', 'inversión', 'dejar', 'sabes', 'punto', 'papeles', 'idea', 'pueda', 'enfermedad', 'privados',   'voluntaria', 'afirma', 'muertes', 'den', 'hablan', 'recibido', 'uds', 'humanidad', 'realmente', 'negociado', 'suerte', 'mayo', 'raro', 'коррумпирован', 'directa', 'dado', 'ja', 'martes', 'medicamento', 'amigo', 'conocer', 'podemos', 'instituto', 'fases', 'septiembre', 'director', 'acceso', 'historia', 'despues', 'horas', 'mostró', 'costo', 'distribución', 'mejores', 'cantidad', 'explica', 'rodríguez', 'p', 'paises', 'nación', 'incluso', 'patria', 'ee', 'edad', 'hija', 'confío', 'comprado', 'tanta', 'finales', 'periodistas', 'busca', 'diferencia', 'deberían', 'apliquen', 'casa', 'polémica', 'pe', '80', 'recién', 'uu', 'comenzó', 'público', 'derecha', 'diario', 'traen', 'desconfianza', 'hagan', 
'señora', 'gusta', 'vale', 'fe', 'vivo', 'unas', 'vacunan', 'seria', 'buscar', '18','diga', 'aplicando', 'quería', 'compran', 'ciudadanos', '9', 'programa', 'loco', 'junto', 'entrevista', 'pacientes', 'i', 'delcy', 'vacune', 'dando', 'tv', 'artículo', 'cuesta', 'doctor', 'rápido', 'san', 'sr', 'che', 'confirma', 'acaba', 'apoyo', 'cabeza', 'usan', 'lilly', 'amp', 'provincia', 'canciller', 'меня', 'abril', 'julio', 'trata', 'transparencia', 'posibilidad', 'publicó', 'fármaco', 'participará', 'vergüenza', 'pregunto', 'anda', 'decisión', 'fecha', '14', 'evidencia', 'ciudad', 'trabajo', 'm', 'esperanza', 'ofrecí', 'aplicada', 'news', 'tambien', 'plata', 'observo', 'próximos', 'grupos', 'produce', 'pesar', 'info', 'sanitario', 'vidas', 'sábado', 'publicación', 'aprobado', 'obvio', 'negociar', 'universal', 'tercer', 'basura', 'último', 'izquierda', 'menor', 'pública', 'sistema', 'apenas', 'positivo', 'resultado', 'jaja', 'superior', 'imagino', 'real', 'mayoría', 'propaganda', 'alto', 'latinoamérica', 'confirman', 'зовут', '0', 'compro', 'querer', 'carla', 
'21', 'desarrollada', 'urgente', 'ex', 'colocarse', 'pienso', 'lucha', 'anuncian', 'poniendo', 'producida', 'recomienda', 'téllez', 'cuerpo', 'sera', 'culpa', 'viernes', 'probará', 'aceptar', 'gestión', 'quiera', 'aires', 'doble', 'aplicaron', 'hijos', 'че', 'hacia', 'confiar', 'redes', 'ok', 'pagar', 'лжец', 'dentro', 'mentiras', 'publicados', 'darse', 'funcionarios', 'почему', 'opción', 'excelente', 'carlos', 'critican', 'даю', 'suficiente', 'completa', 'trabajadores', 'l', 'menores', 'чистые', 'nuevas', 'ciento', 'прямые', 'sekundarioski', 'credibilidad',  'frío', 'reaksionoski', 'decía', 'cuidado', 'иi', 'vi', 'grande', 'награды', 'hará', 'partido', 
'alcanza', 'organismo', 'interés', 'nacionales', 'seguramente', 'medicina', 'informa', 'registrada', 'сеитгюд', 'duque', 'próximo', 'detrás', 'manuel', 'cola', 'muestran', 'meиш', 'pedir', 'dije', 'podrían', 'causa', 'aplican', 'llegado', 'cuánto', 'base', 'sanitaria', 'embargo', 'trankiloski',  'recomendable', 'gob', 'aca', 'iban', 'niños', 'ерпестe', 'miércoles',  'lleva', 'falso', 'аьио', 'afirmó',  'etiqueta', 'listo', 'entiende', 'toca', 'hugo', 'adquirirá', 'ven', 'intereses', 'овут', 'doy', 'traigan', 'jamás', 'participar', 'aseguran', 'masivamente', 'propia', 'libre', 'tarde', 'dias', 'general', 'aval', 'cuentan', 'denuncia', 'sociedad', 'entérate', 're', 'jefe', 'tecnología', 'vienen', 'usando', 't', 'ayuda', 'lee', 'crees', '79', 'volver', 'capacidad', 'dejo', 'riesgos', 'aplique', 'comprando', 'capaz', 'arriba', 'vayan', 'creador', 'piden', 'terminar', 'toduski', 'pones', '2da', 'fácil', 'luz', 'acaso', 'ganas', 'vs', 'conseguir', 'reacción', 'acerca', 'cumple', 'empieza', 'mano', 'mamá', 'secundario', 'negocios', 'tenes', 'saludos', 'foto', 'vieja', 'culo', 'mexicano', 'digan', 'autorizar', 'hdp', 'inicio', 'senadora', 'malo', 'probado', 'cargo', 'produjo', 'querían', 'cerca', 'feliz', 'poca', 'vacunacovid19', 'vuelve', 'vender', 'quieres', 'marcelo', 'llego', 'gratuita', 'piensan', 'hecha', 'incluido', 'compren', 'venden', 'entrega', 'embajador', 'preliminares', 'hacerlo', 'salvar', 'toque', 'alerta', 'pondrá', 'siento', 'noche', 'pq', 'hilo', 'radio', 'aborto', 'российской', 'parecer', 'moral', 'justo', 'piensa', 'viendo', 'федерации', 'república', 'ley', 'negociaciones', 'ignorante', 'ideología', 'meter', 'militar', 'россии', 'vacunarme', 'principios', 'comisión', 'permiso', 'dia', 'diputados', 'control',  'loca',  'suspende', 'deje', 'pidió', 'jorge', 'carrió', 'solución', 'gates', 'comunicación', 'manos', 'fuente', 'región', 'gines', 'iniciar', 'tn', 'acabo', 'habló', 'documento', 'vacunada', 'críticas', 'quieran', 'pocos', 'autorice', 'carajo', 'clarín', 'evitar', 'bastante', 'europeos', 'pura', 'plazo', 'muere', 'brazo', 'puedes', 'requiere', 'simple', 'esperemos', 'pedido', '2oct', 'aparte', 'vacunacion', 'universidad', 'garantizarle', 'salen', 'elegir', 'firmó', 'ganar', 'dudosa', 'demostrado', 'garantizar', 'jugar', 'congreso', 'pena', 'muerto', 'par', 'tenés', 'fila', 'salga', 'veremos', 'ratas', 'necesitan', 'número', 'aqui', 'basta', '4t', 'línea', 'marcha', 'últimos', 'aeropuerto', 'conoce', 'varias', 'quedar', 'acuerdos', 'razones', 'viejo', 'rechazó', 'aprueban', 'totalmente', 'mitad', 'quizás', 'lea', 'equipo', 'propio', 'funcione', 'pdte', 'contrario', 'preocupa', 'comenzar', 'regulador', 'generar', 'reciben', 'libertad', 'porq', 'dato', 'realizar', 'ruleta', 'fake', 'termina', 'condiciones', 'confía', 'juan', 'prioridad', 'ello', 'sigan', 'escándalo', 'necesitamos', 'peligro', 'canal', 'quedó', 'pesos', 'entender', 'alemana', 'joder', 'sigo', 'viva', 'ética', 'mujer', 'presenta', 'apruebe', 'puro', 'supuesto', 'responsable', '13', 'histórico', 'cualquiera', 'sector', 'porcentaje', 'pablo', 'demuestra', 'interesa', 'dejan', 'daño', '400', 'empezó', 'suena', 'secretario', 'inmunológica', 'seriedad', 'combatir', 'fabricantes', 'pondrías', 'willax', 'pondrán', 'aplicarán', 'boca', '23', 'componente', 'covidー19', 'das', 'leí', 'defender', 'criticar', 'registró', 'pocas', 'afirman', 'mirá', 'ponerte', 'encuesta', 'árabes', 'llegaría', 'organismos', 'cuestión', 'comunicado', 'importar', 'serios', 'pondrían', 'adelante', 'beto', 'trajo', 'increíble', 'bla', 'fiebre', 'cerebro', 'r', 'desastre', 'iniciará', 'economía', 'quiso', 'dale', 'navidad', 'sabía', 'cerrar', 'probaron', 'luis', 'idiota', 'encuentra', 'situación', 'colocar', 'osea', 'falsa', 'show', 'dió', 'contar', 'opositores', 'costará', 'cuantos', 'orden', 'sur', 'experimento', 'bill', 'covax', 'compre', 'palabras', 'negociación', 'desinformación', 'americana', 'perdón', 'solamente', 'fabricación', 'fernandez',  'ésta', 'jubilados', 'rechaza', 'comentario', 'piñera', 'turno', 'acto', 'chiste', 'empresas', 'defensa', 'gabinete', 'interesante', 'viejos', 'prefieren', 'esperan', 'aplicado', 'inyectar', 'difícil', 'sirven', 'camino', 'largo', 'adenovirus', 'darle', 'peronista', 'rato', 'peruano', 'negocia', 'urss', 'siga', 'trabaja', 'b', 'carrera', 'morena', 'peruana', 'kicillof', 'sociales', 'diferentes', 'ahi', 'envío', 'deberá', 'privado', 'variantes', 'principio', 'fabricará', 'invimaasesino', 'sepa', 'jajajajaja', 'prestigiosa', 'ofreció', 'escuchar', 'origen', 'atrás', 'nelson', 'zelaya', 'enfermedades', 'fuerte', 'relato', 'toma', 'unido', '38', 'especial', 'supuesta', 'aprobadas', 'error', 'vemos', 'toman', 'protocolo', 'probando', 'eficiente', 'debemos', 'esperamos', 'sputnikvllegaavenezuela', 'social', 'argumentos', 'cinco', 'sacar', 'occidentales', 'criminal', 'suficientes', 'contratos', 'venezolana', 'ministros', 'ignorantes', 'significa', 'solicitud', 'fracaso', 'federal', 'risa', 'peligrosa', 'científicas', 'cero', 'recibirán', 'allí', 'distribuir',  'pensando',  'papá', 'ninguno', 'comentarios', 'hospitales', 'probó', 'empezaron', 'clínica', 'español', 'chavistas', 'eh', 'ridículo', 'haces', 'apta', 'j', 'sandra', '94', 'minutos', 'aprobaron', 'cuales', 'subsecretario', 'últimahora', 'fría', 'periodismo', 'memes', 'miente', 'turquía', 'ponérsela', 'recuerdo', 'protege', 'dra', 'ojos', 'secreto', 'leo', 'maestros', 'mensaje', 'confían', 'floja', 'inútil', 'reino', 'pese', 'ensalada', 'humo', 'paja', 'idiotas', 'podrán', 'fines', 'debes', 'colombiano', 'in', 'andan', 'llamada', 'gasolina', 'europeo', 'ay', 'corona', 'domingo', 'esposa', 'n', 'ultimahora', 'estrategia', 'permite', 'tellez', 'socialista', 'relación', 'dispuesto', 'llevar', 'us', 'entrada', 'media', 'cdmx', 'informes', 'negó', 'faltan', 'traerá', 'dices', 'puedan', 'evaluar', 'light', 'tantas', 'verde', 'políticas', 'seguimos', 'sra', 'llegando', 'pasos', 'junio', 'ademas', 'síntomas', 'pidiendo', 'morado', 'supuestamente', 'véktor', 'beber', 'supera', 'inició', 'preguntas', 'trabajar', 'pase', 'hombre', 'negociando', 'digital', 'respeto', 'pudo', 'mueren', 'estupidez', 'gana', 'supongo', 'aquellos', 'cumplir', 'entrar', 'proyecto', 'sars', 'necesario', 'mínimo', 'quiénes', 'dictadura', '65', 'producto', 'dudo', 'imposible', 'irán', 'daría', 'clases', 'juego', 'entra', 'quejan', '33', '48', 'irresponsable', 'hermana', 'pedro', 'embajada', 'animales', 'titular', 'especialistas', 'documentación', 'colombianos', 'defiende', 'это', 'consecuencias', 'opina', 'aplicarla', 'revisada', 'explican', 'temas', 'venta', 'mentir', 'revisión', 'registra', 'ojala', 'mandatario', 'buscan', 'utilizar', 'compramos', 'éste', 'pendejos', 'chilenos', 'comienzan', 'daniel', 'trajeron', 'principal', 'pendejo', 'ningun', 'declaraciones', 'cubano', 'autoridad', 'buscando', 'hermano', 'señaló', 'dejó', 'obtener', 'locos', 'petición', 'podes', '97', 'putín', 'salieron', 'chairos', 'soviética', 'miserable', 'motivo', 'estadounidense', 'pelotudos', 'suministro', 'advierte', 'coima', 'paulo', 'presidenta', 'anunciado', 'circo', 'viaje', 'común', 'avance', 'demostró', 'organización', 'vino', 'infectólogo', 'xd', 'desarrolladores', 'empresario', 'aviones', 'hablamos', 'experiencia', 'opciones', 'informar', 'relaciones', 'miserables', 'lleguen', 'rechazo', 'explicación', 'guaidó', 'estatal', 'simplemente', 'manejo', 'pasando', 'prevé', 'occidental', 'completo', 'mentiroso', 'tierra', 'dudar', 'comprarla', 'positivos', 'asco', 'preliminar', 'g', 'inyección', 'logística', '27', 'solicitaron', '32', 'funcionó', 'dolor', 'quisiera', 'cuántos', 'fotos', 'aclarar', 'fanb', 'gato', 'valores', 'prestigio', 'richmond', 'caba', 'prevenir', 'posibles', 'geopolítica', 'obviamente', 'clave', 'motivos', 'hacemos', '22', 'empiezan', 'medidas', 'oportunidad', 'genocida', 'sirva', 'dudan', '75', 'mexicana', 'ar', 'digemid', 'onda', 'di', 'demanda', 'oye', 'perder', 'avances', 'querés', 'tenia', 'clase', 'ola', 'darme', '16', 'directo', 'palabra', 'leído', '800', 'seis', 'adn', '28', 'discurso', 'ponernos', 'suma', 'grados', 'siguiente', 'eu', 'dará', 'inútiles', 'hago', 'versión', 'cov', 'juntos', 'próximas', 'vivir', 'prueben', 'gustaría', 'debido', 'responsabilidad', 'mesa', 'flores', 'super', 'calle', 'venir', 'abuela', 'caracas', 'ves', 'terminó', 'crea', 'tantos', 'abre', 'empezará', 'necesidad', 'amiga', 'vive', 'harán', 'cuatro', 'tratamiento', 'territorio', 'quedo', 'dolares', 'león', 'corea', 'servía', 'crear', 'vaina', 'josé', 'certificación', 'prevención', 'cnn', 'pitta', 'crisis', 'acepta', 'confirmado', 'administración', 'quedan', 'ancianos', 'medicos', 'campo', 'precalificación', 'privada', 'america', 'miembros', 'aplicaría', 'enfermera', 'ponte', 'vende', 'casmu', 'sangre', 'justicia', 'asunto', 'amor', 'página', 'humano', 'tranquilo', 'futuro', 'biontech', 'puerta', 'analiza', 'aterriza', 'perfecto', 'hablo', 'vladímir', 'cilia', 'medico', 'explicar', 'variante', 'revela', 'hipocresía', 'uribistas', 'nuevos', 'post', 'segun', 'arg', 'propongo', 'recursos', 'cepas', 'importación', 'amo', 'dicha', 'actual', 'familiares', 'sputinkv', 'manda', 'anunciaron', 'competencia', 'responsables', 'objetivo', 'morales', 'tranquilidad', 'demasiado', 'revistas', 'candidato', 'últimas', 'existen', '31', 'casualidad', 'doctora', 'lejos', 'claves', 'hechos', 'pondré', 'aplico', 'silencio', 'tuit', 'comer', 'santa', 'miren', '5g', 'productos', 'sanidad', 'experimentar', 'aguilar', 'arribó', 'cayetano', 'compras', 'señores', 'don', 'fuerza', 'económica', 'dejaron', 'aumento', 'vzla', '600', 'f', 'habitantes', 'claramente', 'garantiza', '45', 'apuesta', 'debate', 'épica', 'juicio', 'alguno', 'inocular', 'querido', 'contraindicaciones', 'considera', 'extranjeros', 'confidencialidad', 'argumento', 'propone', 'paga', 'trucha', 'falsas', 'escuché', 'sánchez', 'carta', 'cabo', 'compartir', 'dispuestos', 'conozca', 'salvo', 'dura', 'aire', 'ii', 'conozco', 'gripe', 'ofrecieron', 'avalada', 'llamar', 'detalle', 'investigar', 'necesarias', '17', 'cae', 'probarla', 'impuestos', 'prefiere', 'ambos', 'politica', 'vuelta', 'publicar', 'pago', '150', 'etapas', 'publicidad', 
'presentado', 'negro', 'pongas', 'famosa', 'gobernadores',  'mienten', 'famosos', 'actualidad', 'boludos', 'grieta', 'todavia', 'marca', 'recuerda', 'moreno', 'acelerar', 'podía', 'cientificos', 'llevan', 'nacion', 'evalúa', 'padre', 'requisitos', 'importantes', 'proteger', 'aprobaciones', 'necesito', 'explicó', 'negarse', 'públicos', 'costa', 'vea', 'trabajando', 'cuántas', 'deseo', 'uci', 'poquito', 'tweet', 'sanitarias', 'suspendió', 'youtube', 'obliga', 'viru']
