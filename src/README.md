## File Structure

`api` - Glue code to allow communication between different services  
`comp` - Actual code of components for robot functionality  
`serv` - Specific Client/Services instances to start and use components  
`util` - Miscellaneous useful code that doesn't pertain to one system.  

## Code Architecture
Each functionality on the robot is abstracted into various 'services'. These services are simply processes that are waiting for requests to be made, when they receive the request, they will call the appropriate callback. This allows a main program to call any functionality it needs at any time by relaying the appropriate message to the appropriate port. Because of this design decision, the robot is basically split into components. This will include things like control, camera, speech, etc... The code that these services actually run specific to the component can be found in the go folder. There is an API or "glue code" that allows all these different services to talk which can be found in the api folder. Each service is then hosted using the API and can be called with the appropriate request which can be found in the serv folder. Finally, the utility folder simply has tools that aren't specific to any component but add to the functionality of the robot. 
