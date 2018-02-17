function Task(id, des, due, sta)
{
    this.TaskID = id;
    this.Description = des;
    this.DueDate = due;
    this.Status = sta;
}


var tasks = [];



function initTasks()
{
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function()
    {
       if(xhttp.readyState == 4 && xhttp.status == 200)
       {
            var data = xhttp.responseText;
            taskStrings = data.split(";");
            for (var i = 0; i <  taskStrings.length; i++){
                var taskString = taskStrings[i];
                var attributeStrings = taskString.split(",");
                var newTask = new Task(attributeStrings[0],attributeStrings[1],attributeStrings[2],attributeStrings[3]);
                tasks.push(newTask);
            }
            alert("A total of" + tasks.length + "tasks are added to the array");
            addTaskInfoToList();
       }
    }

    xhttp.open("GET", "/loadTasks/", true);
    xhttp.send();
}


function addTaskInfoToList()
{
    if(tasks.length==0)
    {
        alert("Please load the initial drawings to the array first.");
        return;
    }


    var HTMLToDoList = document.getElementById("TodoIDList");
    
    
    HTMLToDoList.innerHTML = "";

    for(var i=0;i<tasks.length;i++)
    {

        var task = tasks[i];

        var newOption = document.createElement("option");
        
        
        newOption.text = task.TaskID;
        
        
        HTMLToDoList.appendChild(newOption);
    }

    alert("A total of "+tasks.length+" drawings are added to the HTML list.");

}

function drawingInfoListChange()
{
    var HTMLTodoList = document.getElementById("TodoIDList");

    // The selectedIndex attribute belongs to any <select> tag.
    // It represents the current index of the selected item.
    var TodoIndex = HTMLTodoList.selectedIndex;

    // Since the items in the drawinginfoList is the same order
    // as the drawings list, the index of the selected item also represents
    // the index of the drawing item in the array.
    var selectedtask = tasks[TodoIndex];


    // Now we can use this selected object of the drawing to update the
    // drawing information.
    document.getElementById("descriptionInput").value = selectedtask.Description;
    document.getElementById("dueDateInput").value = selectedtask.DueDate;
    console.log(selectedtask.Status);
    if(selectedtask.Status == "True")
    {
        document.getElementById("statusInput").checked = true;
    }
    else
    {
        document.getElementById("statusInput").checked = false;
    }
    
    // Task 1.d, please use the information in selectedDrawing to finish the 
    // five <input> tags.

}



function addTask()
{
    var descriptionText = document.getElementById("descriptionInput").value;
    var dueDateText = document.getElementById("dueDateInput").value;
    var statusText = document.getElementById("statusInput").value;

    var xhttp = new XMLHttpRequest();
    var getNewIDWindow = prompt("Please enter a new ID for the Task", "");
    xhttp.onreadystatechange = function()
    {
        if(xhttp.readyState == 4 && xhttp.status == 200)
        {
        	if(xhttp.responseText == "false")
        	{
        	    var newID = getNewIDWindow;
        		var xhttp2 = new XMLHttpRequest();
        		var sendParameters = "?TaskID=" + newID + "&Description=" +  descriptionText
                + "&DueDate=" + dueDateText + "&Status=" + statusText;
                xhttp2.open("GET", "/addTask/"+sendParameters, true);
                xhttp2.send();
                var newTask = new Task(newID, descriptionText, dueDateText, statusText);
                tasks.push(newTask);
                addTaskInfoToList();
        	}
            else
            {
            	alert("This ID exists. Please enter a new one.");
            }
        }
    };
    xhttp.open("GET", "/checkID/"+"?TaskID="+getNewIDWindow, true);
    xhttp.send();

}