#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project -> File   ：py-errors -> error
@IDE    ：PyCharm
@Author ：sven
@Date   ：2022/2/17 16:13
@Desc   ：
"""
import enum


class BizError(RuntimeError):
    """
    业务异常
    """
    __slots__ = "error_code", "error_value", "error_remark"

    def __init__(self, error_code, error_value, error_remark=None, *args):
        """

        :param error_code: 错误码
        :param error_value: 错误值
        :param error_remark: 错误详细信息
        :param args:
        """
        self.error_code = error_code
        self.error_value, self.error_remark = error_value, error_value
        if error_remark:
            self.error_remark = error_remark
            if args:
                self.error_remark = self.error_remark.format(*args)

    def __str__(self):
        """
        @overide
        :return:
        """
        return f"error_code={self.error_code}," \
               f" error_value={self.error_value}," \
               f" error_remark={self.error_remark}"

    def as_dict(self):
        """

        :return:
        """
        return {
            "error_code" : self.error_code,
            "error_value" :self.error_value,
            "error_remark" : self.error_remark
        }


class IError(enum.Enum):
    """
    异常
    """
    def exception(self, error_remark=None, *args):
        """
        异常
        :param msg:
        :param args:
        :return: BizError对象
        """
        return BizError(self.value, self.name, error_remark, *args)

    def reraise(self, error_remark=None, *args):
        """
        抛出异常
        :param remark:
        :param args:
        :return:
        """
        raise self.exception(error_remark, *args)

    def __call__(self, error_remark=None, *args):

        return self.exception(error_remark, *args)


@enum.unique
class errors(IError):
    PROGRAMMING_ERROR = 9999
    VALIDATE_ERROR = 1000


if __name__ == '__main__':
    error = errors.PROGRAMMING_ERROR('编码错误')
    error1 = errors.VALIDATE_ERROR('参数id必填')
    print(error1)
    print(error)