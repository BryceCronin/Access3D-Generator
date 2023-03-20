
# Access3D Custom Device Generator
This is a fully functional proof-of-concept app created for the [ELC Accessible Beauty Hackathon](https://elchackathon.devpost.com/).
For more information on this project, please visit the [Access3D Generator Devpost page](https://devpost.com/software/wip-wo4d6r).

## Project Status
To make Access3D Generator as accessible as possible, I am working to move Access3D Generator to the web.  This will remove the need for the below setup process, which some users may find complicated. This will be completed after the conclusion of the ELC Accessible Beauty Hackathon.

## Requirements

 - Currently, Access3D Generator will run only on Windows.
 - Access3D Generator relies on [OpenSCAD](https://openscad.org/), and as such it must be installed on your device.
	 - Ensure that the installed OpenSCAD folder is listed under 'Path' in your System Variables. This is extremely important.
![Setting path](https://i.imgur.com/TCpVrov.png)
	 - This can be confirmed by running the `openscad --version` command.

## How it works
For a demonstration on how this app works, please visit the [Access3D Generator Devpost page](https://devpost.com/software/wip-wo4d6r).

## Creating an A3D file
An A3D file is simply a SCAD file with additional information that can be read by Access3D Generator. After defining variables as normal, you can include additional information between the `//A3D-Start` and `//A3D-End` tags. To maintain backwards compatibility with SCAD files, all A3D info between these tags should be commented. A3D files currently support integers and booleans. All measurements are in mm.

Each customisation option follows the following format:

 - "Integer" or "Boolean".
 - Existing variable name between [] brackets.
 - User friendly variable name between <> brackets.
 - User friendly description between {} brackets.

An example of what this looks like is:

    // A3D-Start
    // Integer [jardiameter]<Lid Diameter>{The size of the cosmetics jar lid (mm)}
    // Integer [gripdiameter]<Grip Diameter>{How large would you like the grip to be? (mm)}
    // Integer [gripheight]<Grip Height>{How tall would you like the grid to be? (mm)}
    // Boolean [gripdots]<Grip Dots>{Include extra grip?}
    // A3D-End

You can view the A3D_Sample_Files folder for more examples.

The next version of Access3D Generator will use JSON instead of the above standard. This will allow for far greater control and additional options.
