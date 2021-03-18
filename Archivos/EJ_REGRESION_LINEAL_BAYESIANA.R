"install.packages('ISLR')
install.packages('caret')
install.packages('arm')
install.packages('Ecdat')
install.packages('gridExtra')"

"Librerias que nos facilitaran la creacion de los modelos predictivos,
creacion de graficos y conjunto de datos econometricos"
library(ISLR);library(caret);library(arm);library(Ecdat);library(gridExtra)

data("Hedonic") #llamando a la base de datos
#Creando particiones de la base de datos para analisis posteriores
inTrain<-createDataPartition(y=Hedonic$tax,p=0.7, list=FALSE)
trainingset <- Hedonic[inTrain, ]
testingset <- Hedonic[-inTrain, ]
#mostrando la base de datos 
str(Hedonic)

#CREANDO MODELO DE REGRESION NORMAL LINEAL
ols.reg<-lm(tax~.,trainingset)
summary(ols.reg)

"Hacemos nuestra predicción y compararemos los resultados con el conjunto de prueba utilizando: 
correlación, estadísticas de resumen y el error absoluto medio"
ols.regTest<-predict.lm(ols.reg,testingset,interval = 'prediction',se.fit = T)
#correlacion
cor(testingset$tax,ols.regTest$fit[,1])
#estadisticos de resumen
summary(ols.regTest$fit[,1])
summary(trainingset$tax)
#error absoluto medio 
MAE<-function(actual, predicted){
  mean(abs(actual-predicted))
}
MAE(ols.regTest$fit[,1], testingset$tax)

#variables utilizadas para formar el grafico
yout.ols <- as.data.frame(cbind(testingset$tax,ols.regTest$fit))
ols.upr <- yout.ols$upr
ols.lwr <- yout.ols$lwr
#creando grafico con las variables anteriores
p.ols <- ggplot(data = yout.ols, aes(x = testingset$tax, y = ols.regTest$fit[,1])) + geom_point() + ggtitle("Ordinary Regression") + labs(x = "Actual", y = "Predicted")
p.ols + geom_errorbar(ymin = ols.lwr, ymax = ols.upr)


#creando el modelo de regresion bayesiana
bayes.reg<-bayesglm(tax~.,family=gaussian(link=identity),trainingset,prior.df = Inf)
bayes.regTest<-predict.glm(bayes.reg,newdata = testingset,se.fit = T)
#correlacion
cor(testingset$tax,bayes.regTest$fit)
#resumen estadisticos
summary(bayes.regTest$fit)
#error cuadratico medio
MAE(bayes.regTest$fit, testingset$tax)

#calculando intervalo de confianza para el bayesiano, y asignando pametros a utilizar en la grafica
yout.bayes <- as.data.frame(cbind(testingset$tax,bayes.regTest$fit))
names(yout.bayes) <- c("tax", "fit")
critval <- 1.96 #approx for 95% CI
bayes.upr <- bayes.regTest$fit + critval * bayes.regTest$se.fit
bayes.lwr <- bayes.regTest$fit - critval * bayes.regTest$se.fit
#creando grafico de regresion bayesiana
p.bayes <- ggplot(data = yout.bayes, aes(x = yout.bayes$tax, y = yout.bayes$fit)) + geom_point() + ggtitle("Bayesian Regression Prediction") + labs(x = "Actual", y = "Predicted")

#una vez creadas ambas graficas de las regresiones, se muestran en modo de comparacion
ols.plot <-  p.ols + geom_errorbar(ymin = ols.lwr, ymax = ols.upr)
bayes.plot <-  p.bayes + geom_errorbar(ymin = bayes.lwr, ymax = bayes.upr)
grid.arrange(ols.plot,bayes.plot,ncol=2)

"""
conclusion: 
El enfoque bayesiano proporciona intervalos de confianza más compactos.
 
reduce la varianza y fortalece la confianza que podemos tener en cada ejemplo individual.
URL:https://educationalresearchtechniques.com/2017/10/18/linear-regression-vs-bayesian-regression/
"""
