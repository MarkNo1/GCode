
## XML

The Xml class is an easy way of writing Xml files using
Dictionary as data.

**Structure**:

The data that should be passed to the class shoud contains this four
keys : root*, args , body ,xmls

```python

data = dict(root='name')

```

'*' mandatory.

  - **root**  

Name
```xml
<library>
```

  - **args**

Variables
```xml
<library> name="Name of the lib"
```

  - **body**

Description
```xml
<library>
       BODY
</library>
```

  - **xmls**

Nested XML

```xml
<library>
        <class/>
</library>
```

### How to use

All you need is Dictionary to pass the data into Xml.

Example:

```python

descriptionData = dict(root='description', body='This is the description.')

classData = dict ( root='class',
                   args = dict(
                            name="perception/HexagonsGrid",
                            type="renault_nodelets::HexagonsGrid",
                            base_class_type="nodelet::Nodelet"),
                    xmls = [descriptionData]))

libraryData = dict( root='libray',
                 args= dict(path="lib/libhexagrid_nodelet"),
                 xmls=[classData]))

xml = Xml(libraryData)

print(xml.generate())

```
Result

```xml

<libray path=lib/libhexagrid_nodelet>


	<class name=perception/HexagonsGrid type=renault_nodelets::HexagonsGrid base_class_type=nodelet::Nodelet>


		<description>
		Description of the class
		</description>
	</class>
</libray>

```

Don't worry, is ridiculusly tedius to write this Dictionary by hand,
infact we are going to automitize the process.  


D = Dictionary

des_x = D(root='description', body='Description of the class')

class_x = D(    root='class',
                args= D(
                  name="perception/HexagonsGrid",
                  type="renault_nodelets::HexagonsGrid",
                  base_class_type="nodelet::Nodelet"),
                xmls=[des_x])

lib_x = D(root='libray',args=D(path="lib/libhexagrid_nodelet"), xmls=[class_x])

xml = Xml(lib_x)
