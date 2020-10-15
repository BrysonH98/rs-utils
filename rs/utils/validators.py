# rs-utils is available under the MIT License. https://gitlab.com/roundservices/rs-utils/
# Copyright (c) 2020, Round Services LLC - https://roundservices.biz/
#
# Author: Ezequiel O Sandoval - esandoval@roundservices.biz
#


def validate_or_raise_for_value(boolean_value, logger, msg, *args):
	"""
	If the boolean value received is false, it will throw a ValueError, and raise an error
	:param boolean_value:
	:param logger: RoundServices log - if None, will not log just throw error to default output
	:param msg: in case of error, it is a template
	:param args: params from msg
	:return: raise an error
	"""
	if not boolean_value:
		error_msg = msg.format(*args) if len(args) > 0 else msg
		if logger is not None:
			logger.error(error_msg)
		raise ValueError(error_msg)


def raise_and_log(logger, exception, msg, *args):
	"""
	Logs error in rs_log object, then raise an exception
	:param logger: rs_obj
	:param exception: Python Error class to raise
	:param msg: template or full msg to log
	:param args: parameters if msg is a string template
	:return:
	"""
	error_msg = msg.format(*args) if len(args) > 0 else msg
	logger.error(error_msg)
	raise exception(error_msg)


