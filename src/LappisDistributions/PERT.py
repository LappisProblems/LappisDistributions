#Defining the PERT class
class PERT:

    #Define the PERT probability density function
    def pdf(x, a, b, c):
        #Firstly, ensure that parameters are specified correctly
        if a>=b:
            raise ValueError('a is equal to or larger than b, it should be smaller')
        if b>=c:
            raise ValueError('b is equal to or larger than c, it should be smaller')
        if x<a or x>c:
            raise ValueError('Selected value for the variable lies outside of support')
        
        #Now alpha and beta will be calculated.
        alpha=(4*b+c-5*a)/(c-a)
        beta=(5*c-a-4*b)/(c-a)
        
        #Define PDF, function returns the probability of x
        pdf = ((x-a)**(alpha-1)*(c-x)**(beta-1))/(scipy.special.beta(alpha, beta)*(c-a)**(alpha+beta-1))
        return pdf

    #Define the PERT cumulative density function
    def cdf(x, a, b, c):
        #Firstly, ensure that parameters are specified correctly
        if a>=b:
            raise ValueError('a is equal to or larger than b, it should be smaller')
        if b>=c:
            raise ValueError('b is equal to or larger than c, it should be smaller')
        if x<a or x>c:
            raise ValueError('Selected value for the variable lies outside of support')

        #Now alpha and beta will be calculated.
        alpha=(4*b+c-5*a)/(c-a)
        beta=(5*c-a-4*b)/(c-a)
        
        #Calculate z for the incomplete beta function
        z=(x-a)/(c-a)

        #Define CDF, function returns P(X<=x)
        cdf=scipy.special.betainc(alpha, beta, z)
        return cdf
    
    #Define the PERT mean
    def mean(a, b, c):
        #Firstly, ensure that parameters are specified correctly
        if a>=b:
            raise ValueError('a is equal to or larger than b, it should be smaller')
        if b>=c:
            raise ValueError('b is equal to or larger than c, it should be smaller')
        if x<a or x>c:
            raise ValueError('Selected value for the variable lies outside of support')
        
        mean=(a+4*b+c)/6
        return mean
    
    #Define the PERT median
    def medi(a, b, c):
        #Firstly, ensure that parameters are specified correctly
        if a>=b:
            raise ValueError('a is equal to or larger than b, it should be smaller')
        if b>=c:
            raise ValueError('b is equal to or larger than c, it should be smaller')
        if x<a or x>c:
            raise ValueError('Selected value for the variable lies outside of support')

        #Now alpha and beta will be calculated.
        alpha=(4*b+c-5*a)/(c-a)
        beta=(5*c-a-4*b)/(c-a)

        #Calculate median
        medi=scipy.special.betainc(alpha, beta, 0.5)**(-1) * (c-a)+a
        return medi
    
    #Define the PERT mode
    def mode(b):
        #Firstly, ensure that parameters are specified correctly
        if a>=b:
            raise ValueError('a is equal to or larger than b, it should be smaller')
        if b>=c:
            raise ValueError('b is equal to or larger than c, it should be smaller')
        if x<a or x>c:
            raise ValueError('Selected value for the variable lies outside of support')
        
        return b
    
    #Define the PERT variance
    def vari(a, b, c):
        #Firstly, ensure that parameters are specified correctly
        if a>=b:
            raise ValueError('a is equal to or larger than b, it should be smaller')
        if b>=c:
            raise ValueError('b is equal to or larger than c, it should be smaller')
        if x<a or x>c:
            raise ValueError('Selected value for the variable lies outside of support')

        #Calculate
        mu=PERT.mean(a, b, c)

        #Calculate variance
        vari=((mu-a)*(c-mu))/7
        return vari

    #Define the PERT Skewness
    def skew(a, b, c):
        #Firstly, ensure that parameters are specified correctly
        if a>=b:
            raise ValueError('a is equal to or larger than b, it should be smaller')
        if b>=c:
            raise ValueError('b is equal to or larger than c, it should be smaller')
        if x<a or x>c:
            raise ValueError('Selected value for the variable lies outside of support')

        #Now alpha and beta will be calculated.
        alpha=(4*b+c-5*a)/(c-a)
        beta=(5*c-a-4*b)/(c-a)

        #Calculate skewness
        skew=(2*(beta-alpha)*np.sqrt(alpha+beta+1))/((alpha+beta+2)*np.sqrt(alpha*beta))
        
        return skew
        
    #Define the PERT Ex. kurtosis
    def exku(a,b,c):
        #Firstly, ensure that parameters are specified correctly
        if a>=b:
            raise ValueError('a is equal to or larger than b, it should be smaller')
        if b>=c:
            raise ValueError('b is equal to or larger than c, it should be smaller')
        if x<a or x>c:
            raise ValueError('Selected value for the variable lies outside of support')
        
        #Now alpha and beta will be calculated.
        alpha=(4*b+c-5*a)/(c-a)
        beta=(5*c-a-4*b)/(c-a)

        #Calculate ex. kurtosis
        exku=(6*((alpha-beta)**2*(alpha+beta+1)-alpha*beta*(alpha+beta+2)))/(alpha*beta*(alpha+beta+2)*(alpha+beta+3))
        return exku
