
function changeSessionInfo()
{
    // var ra_name = document.getElementById('ra_name');
    var experiment_name = document.getElementById('experiment_name');
    var participant_number = document.getElementById('participant_number');
    
    // ra_name.readOnly = false;
    experiment_name.readOnly = false;
    participant_number.readOnly = false;
}

function toggleElement(eID)
{
    var elementBlock = document.getElementById(eID);
    if (elementBlock.style.display === "block")
    {
        elementBlock.style.display = "none";
    }
    else if (elementBlock.style.display = "none")
    {
        elementBlock.style.display = "block";
    }
}

