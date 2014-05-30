package io.github.mhelper.comeworld;

import org.bukkit.command.Command;
import org.bukkit.command.CommandSender;
import org.bukkit.plugin.java.JavaPlugin;

public final class comeworld extends JavaPlugin {
	@Override
	public void onEnable() {
		getLogger().info("onEnable has been invoked!");
	}
 
	@Override
	public void onDisable() {
		getLogger().info("onDisable has been invoked!");
	}
	
	
	@Override
	public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args) {
		if (cmd.getName().equalsIgnoreCase("says")) { // If the player typed /basic then do the following...
			// doSomething
			sender.sendMessage("Hello there!");
			return true;
		} //If this has happened the function will return true. 
	        // If this hasn't happened the value of false will be returned.
		return false; 
	}
}