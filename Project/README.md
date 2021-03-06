# EmotionalSynthesis

This is the emotional synthesis component of an intelligent interactive system project developed by Team-22 for the Intelligent Interactive Systems course held at Uppsala University.

Emotional expressions are artificially synthesized from machine learning processed computer vision input emotion data representing any one of the following six basic human emotions: 

* Anger
* Disgust
* Fear
* Happiness
* Sadness
* Surprise

Each artificial emotional expression generated can be displayed on each of a IrisTK virtual humanoid face and a NAO robot. 

## Team-22

* [Hakami, Farangis](https://github.com/farangiis)
* [Remmers, Alexis](https://github.com/Thizizmyname)
* [Ross, Adam](https://github.com/R055A)

## Instructions

#### Requirements

The following are required for displaying the synthesized emotional expressions:

* [Choregraphe - for NAO robot](http://doc.aldebaran.com/2-4/software/choregraphe/choregraphe_overview.html)
* [IrisTK - for virtual humanoid face](http://www.iristk.net/)

The following are required for running the pipeline application:

* [python 2.7](https://www.python.org/download/releases/2.7/)
* [pynaoqi](http://doc.aldebaran.com/2-5/dev/python/install_guide.html)

Prior to running the pipeline, the [gestures.fxml](https://github.com/R055A/IntelligentaMaskiner/blob/master/Project/emotional_synthesis/virtual_human/gestures/) file is required to be placed in

```
../IrisTK/addon/Face/
```

#### Demonstration

From this directory, enter the following command in a terminal

```
python emotional_synthesis/pipeline -d
```

or, if using any NAO port aside from the fixed ```9559``` port

```
python emotional_synthesis/pipeline -p [NAO port] -d
```

#### From file

Place the text file in the following path

```
..\emotional_synthesis\data\
```

From this directory, enter the following command in a terminal

```
python emotional_synthesis/pipeline -f <file>
```

or, if using any NAO port aside from the fixed ```9559``` port

```
python emotional_synthesis/pipeline -p [NAO port] -f <file>
```

#### User input

From this directory, enter the following command in a terminal

```
python emotional_synthesis/pipeline
```

or, if using any NAO port aside from the fixed ```9559``` port

```
python emotional_synthesis/pipeline -p [NAO port]
```



