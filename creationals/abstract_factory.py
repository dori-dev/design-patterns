"""
Car
    Benz
        Suv   => gla | glc
        Coupe => cls | E-class
    BMW
        Suv   => x1  | x2
        Coupe => m2  | m4
"""
from abc import ABC, abstractmethod


# Car Company

class Car(ABC):
    @abstractmethod
    def call_suv(self):
        pass

    @abstractmethod
    def call_coupe(self):
        pass


class Benz(Car):
    @staticmethod
    def call_suv(model):
        return model

    @staticmethod
    def call_coupe(model):
        return model


class BMW(Car):
    @staticmethod
    def call_suv(model):
        return model

    @staticmethod
    def call_coupe(model):
        return model


# Car Classification

class Suv(ABC):
    @abstractmethod
    def creating_suv(self):
        pass


class Coupe(ABC):
    @abstractmethod
    def creating_coupe(self):
        pass


# Car Models

class Gla(Suv, Benz):
    def creating_suv(self):
        print('This is your suv benz, gla model...')


class Glc(Suv, Benz):
    def creating_suv(self):
        print('This is your suv benz, glc model...')


class X1(Suv, BMW):
    def creating_suv(self):
        print('This is your suv bmw, x1 model...')


class X2(Suv, BMW):
    def creating_suv(self):
        print('This is your suv bmw, x2 model...')


class Cls(Coupe, Benz):
    def creating_coupe(self):
        return print('This is your coupe benz, cls model....')


class EClass(Coupe, Benz):
    def creating_coupe(self):
        return print('This is your coupe benz, E-class model....')


class M2(Coupe, BMW):
    def creating_coupe(self):
        return print('This is your coupe bmw, m2 model....')


class M4(Coupe, BMW):
    def creating_coupe(self):
        return print('This is your coupe bmw, m4 model....')


# Orders

def order_suv(company: Car, model: Suv):
    model_name = model().__class__.__name__
    company_name = company().__class__.__name__
    if issubclass(model, company):
        company: Car = company()
        model: Suv = model()
        suv: Suv = company.call_suv(model)
        try:
            suv.creating_suv()
        except AttributeError:
            raise ValueError(f"{model_name} is not a suv car!")
    else:
        raise NameError(f"{model_name} is not a {company_name} car!")


def order_coupe(company: Car, model: Coupe):
    model_name = model().__class__.__name__
    company_name = company().__class__.__name__
    if issubclass(model, company):
        company: Car = company()
        model: Coupe = model()
        coupe: Coupe = company.call_coupe(model)
        try:
            coupe.creating_coupe()
        except AttributeError:
            raise ValueError(f"{model_name} is not a coupe car!")
    else:
        raise NameError(f"{model_name} is not a {company_name} car!")


if __name__ == '__main__':
    order_coupe(Benz, Cls)
    order_coupe(Benz, EClass)
    order_coupe(BMW, M2)
    order_coupe(BMW, M4)
    order_suv(BMW, X1)
    order_suv(BMW, X2)
    order_suv(Benz, Gla)
    order_suv(Benz, Glc)
    # order_coupe(Benz, Gla)
    # order_coupe(BMW, Cls)
    # order_suv(Benz, Cls)
    # order_suv(BMW, Gla)
