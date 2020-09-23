function toggleMenu()
{
    var curtain = document.getElementById('curtain');
    var menu = document.getElementById('menu');
    
    if (curtain.style.display === "none")
    {
        curtain.style.display = "block";
        menu.style.display = "block";        
    }
    else if(curtain.style.display === "block")
    {
        curtain.style.display = "none";
        menu.style.display = "none";
    }
}

function closeNotif()
{
    var notifBox = document.getElementById('notifBox');
    var notifHeader = document.getElementById('notifHeader');
    notifBox.style.display = "none";
    notifHeader.style.display = "none";
}