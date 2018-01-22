

package com.peergine.tool;

import java.util.Scanner;
import java.io.File;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import com.peergine.plugin.pgJNINode;
import com.peergine.applib.pgErrCode;
import com.peergine.webclient.pgWebClient;


public class pgTunnelSvrTool {

	public static void OutString(String sOut) {
		System.out.println(sOut);
	}

	// ParseInt function
	public static int ParseInt(String sInt, int iDef) {
		try {
			if (sInt.equals("")) {
				return 0;
			}
			return Integer.parseInt(sInt);
		}
		catch (Exception ex) {
			return iDef;
		}
	}

	private pgWebClient m_webClient = null;

	public pgTunnelSvrTool() {
	}

	public void Run(String sCfgPath) {
		try {
			m_webClient = new pgWebClient();
			if (!m_webClient.Start(sCfgPath)) {
				return;
			}
//			CmdProc();

//			m_webClient.Stop();
//			m_webClient = null;
		}
		catch (Exception ex) {
		}
	}

	public void Stop(){
		m_webClient.Stop();
		m_webClient = null;
	}

	private void CmdProc() {

		Scanner scanner = new Scanner(System.in);
		while (true) {
			
			System.out.print("> ");
			scanner.hasNextLine();

			String sInput = scanner.nextLine();
			if (sInput.equals("quit")) {
				break;
			}

			String[] sStrArray = sInput.split(" ");
			if (sStrArray.length <= 0) {
				continue;
			}

			if (sStrArray[0].equals("user-add")) {
				if (sStrArray.length < 3) {
					OutString("No enough parameters");
				}
				else {
					UserAdd(sStrArray[1], sStrArray[2]);
				}
			}
			else if (sStrArray[0].equals("user-delete")) {
				if (sStrArray.length < 2) {
					OutString("No enough parameters");
				}
				else {
					UserDelete(sStrArray[1]);
				}
			}
			else if (sStrArray[0].equals("user-setpass")) {
				if (sStrArray.length < 3) {
					OutString("No enough parameters");
				}
				else {
					UserSetPass(sStrArray[1], sStrArray[2]);
				}
			}
			else if (sStrArray[0].equals("user-search")) {
				if (sStrArray.length < 2) {
					OutString("No enough parameters");
				}
				else {
					UserSearch(sStrArray[1], 1);
				}
			}
			else if (sStrArray[0].equals("user-list")) {
				if (sStrArray.length < 3) {
					OutString("No enough parameters");
				}
				else {
					int iSize = ParseInt(sStrArray[1], 1);
					int iPos = ParseInt(sStrArray[2], 0);
					UserList(iSize, iPos, 1);
				}
			}
			else if (sStrArray[0].equals("user-connect")) {
				if (sStrArray.length < 2) {
					OutString("No enough parameters");
				}
				else {
					UserGetChannel(sStrArray[1]);
				}
			}
			else if (sStrArray[0].equals("online-search")) {
				if (sStrArray.length < 2) {
					OutString("No enough parameters");
				}
				else {
					UserSearch(sStrArray[1], 0);
				}
			}
			else if (sStrArray[0].equals("online-list")) {
				if (sStrArray.length < 3) {
					OutString("No enough parameters");
				}
				else {
					int iSize = ParseInt(sStrArray[1], 1);
					int iPos = ParseInt(sStrArray[2], 0);
					UserList(iSize, iPos, 0);
				}
			}
			else if (sStrArray[0].equals("user-add-file")) {
				if (sStrArray.length < 2) {
					OutString("No enough parameters");
				}
				else {
					UserAddFile(sStrArray[1]);
				}
			}
			else if (sStrArray[0].equals("user-delete-file")) {
				if (sStrArray.length < 2) {
					OutString("No enough parameters");
				}
				else {
					UserDeleteFile(sStrArray[1]);
				}
			}
			else {
				OutString("   quit                               Quit this program");
				OutString("   user-add            <user> <pass>  Add one user");
				OutString("   user-delete         <user>         Delete one user");
				OutString("   user-setpass        <user> <pass>  Modify user password");
				OutString("   user-search         <user>         Search user by user name");
				OutString("   user-list           <size> <pos>   List users by size and positon");
				OutString("   user-connect        <user>         Get user's connect info");
				OutString("   online-search       <user>         Search online user by user name");
				OutString("   online-list         <size> <pos>   List online users by size and positon");
				OutString("   user-add-file       <filepath>     Add user list from file");
				OutString("   user-delete-file    <filepath>     Delete user list from file");
			}

			OutString("");
		}
	}
		
	public int UserAdd(String sUser, String sPass) {
		String sData = "64:(User){" + m_webClient.GetNode().omlEncode(sUser) + "}(Pass){"
			+ m_webClient.GetNode().omlEncode(sPass) + "}(Email){test@pptun.com}(Type){0}";
		int iReqID = m_webClient.Request(sData, "");
		if (iReqID < 0) {
			int iErr = -iReqID;
			OutString("   iErr: " + iErr);
		}
		else {
			m_webClient.GetResult(iReqID);
		}
		return iReqID;
	}

    public int UserDelete(String sUser) {
		String sData = "65:(User){" + m_webClient.GetNode().omlEncode(sUser) + "}";
		int iReqID = m_webClient.Request(sData, "");
		if (iReqID < 0) {
			int iErr = -iReqID;
			OutString("   iErr: " + iErr);
		}
		else {
			m_webClient.GetResult(iReqID);
		}
		return iReqID;
	}

    public void UserSetPass(String sUser, String sPass) {
		String sData = "66:(User){" + sUser + "}(Field){Pass}(Value){"
			+ m_webClient.GetNode().omlEncode(sPass) + "}";
		int iReqID = m_webClient.Request(sData, "");
		if (iReqID < 0) {
			int iErr = -iReqID;
			OutString("   iErr: " + iErr);
		}
		else {
			m_webClient.GetResult(iReqID);
		}
	}
	
	private void UserGetChannel(String sUser) {
		String sData = "74:(User){" + m_webClient.GetNode().omlEncode(sUser) + "}";
		int iReqID = m_webClient.Request(sData, "");
		if (iReqID < 0) {
			int iErr = -iReqID;
			OutString("   iErr: " + iErr);
		}
		else {
			int iInd = 0;
			String sResData = m_webClient.GetResult(iReqID);
			while (true) {
				String sEle = m_webClient.GetNode().omlGetEle(sResData, "", 1, iInd);
				if (sEle.equals("")) {
					break;
				}
				
				String sUser1 = m_webClient.GetNode().omlGetName(sEle, "");
				String sThrough = m_webClient.GetNode().omlGetContent(sEle, ".Through");
				String sAddrLcl = m_webClient.GetNode().omlGetContent(sEle, ".AddrLcl");
				String sAddrRmt = m_webClient.GetNode().omlGetContent(sEle, ".AddrRmt");
				String sTunnelLcl = m_webClient.GetNode().omlGetContent(sEle, ".TunnelLcl");
				String sTunnelRmt = m_webClient.GetNode().omlGetContent(sEle, ".TunnelRmt");
				String sTime = m_webClient.GetNode().omlGetContent(sEle, ".Time");
				OutString("   User=" + sUser1 + ", Through=" + sThrough + ", AddrLcl=" + sAddrLcl
					+ ", AddrRmt=" + sAddrRmt + ", TunnelLcl=" + sTunnelLcl + ", TunnelRmt=" + sTunnelRmt + ", Time=" + sTime);
				
				iInd++;
			}
		}
	}

	private int UserSearch(String sUser, int iRegister) {
		String sData = "70:(Field){" + ((iRegister != 0) ? "User" : "Online")
			+ "}(Value){" + sUser + "}(Size){1}(Pos){0}";
		int iReqID = m_webClient.Request(sData, "");
		if (iReqID < 0) {
			int iErr = -iReqID;
			OutString("   iErr: " + iErr);
		}
		else {
			int iInd = 0;
			String sResData = m_webClient.GetResult(iReqID);
			while (true) {
				String sEle = m_webClient.GetNode().omlGetEle(sResData, "", 1, iInd);
				if (sEle.equals("")) {
					break;
				}
				
				String sTemp = m_webClient.GetNode().omlGetName(sEle, "");
				if (sTemp.equals("TotalCount")) {
					String sCount = m_webClient.GetNode().omlGetContent(sEle, "");
					OutString("   OnlineUser count: " + sCount);
				}
				else {
					String sUser1 = m_webClient.GetNode().omlGetContent(sEle, ".User");
					String sClient = m_webClient.GetNode().omlGetContent(sEle, ".Client");
					String sAddr = m_webClient.GetNode().omlGetContent(sEle, ".Addr");
					OutString("   User=" + sUser1 + "\t\tClient=" + sClient + "\tAddr=" + sAddr);
				}
				
				iInd++;
			}
		}
		return iReqID;
	}

	public void UserList(int iSize, int iPos, int iRegister) {
		String sData = "70:(Field){" + ((iRegister!= 0) ? "User" : "Online")
			+ "}(Value){}(Size){" + iSize + "}(Pos){" + iPos + "}";
		int iReqID = m_webClient.Request(sData, "");
		if (iReqID < 0) {
			int iErr = -iReqID;
			OutString("   iErr: " + iErr);
		}
		else {
			int iInd = 0;
			String sResData = m_webClient.GetResult(iReqID);
			while (true) {
				String sEle = m_webClient.GetNode().omlGetEle(sResData, "", 1, iInd);
				if (sEle.equals("")) {
					break;
				}
				
				String sTemp = m_webClient.GetNode().omlGetName(sEle, "");
				if (sTemp.equals("TotalCount")) {
					String sCount = m_webClient.GetNode().omlGetContent(sEle, "");
					OutString("   OnlineUser count: " + sCount);
				}
				else {
					String sUser1 = m_webClient.GetNode().omlGetContent(sEle, ".User");
					String sClient = m_webClient.GetNode().omlGetContent(sEle, ".Client");
					String sAddr = m_webClient.GetNode().omlGetContent(sEle, ".Addr");
					OutString("   User=" + sUser1 + "\t\tClient=" + sClient + "\tAddr=" + sAddr);
				}

				iInd++;
			}
		}
	}

	private void UserAddFile(String sPath) {
		try {
			File file = new File(sPath);
			FileInputStream is = new FileInputStream(file);
			InputStreamReader isr = new InputStreamReader(is);
			BufferedReader in = new BufferedReader(isr);

			int iCount = 0;
			String sLine = null;
			while ((sLine = in.readLine()) != null) {
				String sLineTemp = sLine.trim();
				
				String sUser = "";
				String sPass = "";
				String[] sSect = sLineTemp.split(" ", 2);
				if (sSect.length == 1) {
					sUser = sSect[0].trim();
				}
				else if (sSect.length == 2) {
					sUser = sSect[0].trim();
					sPass = sSect[1].trim();
				}
				else {
					continue;
				}

				String sData = "64:(User){" + m_webClient.GetNode().omlEncode(sUser)
					+ "}(Pass){" + m_webClient.GetNode().omlEncode(sPass) + "}(Email){test@pptun.com}(Type){0}";
				int iReqID = m_webClient.Request(sData, "");
				if (iReqID < 0) {
					int iErr = -iReqID;
					OutString("   iErr: " + iErr);
				}
				else {
					m_webClient.GetResult(iReqID);
					iCount++;
					OutString("   Add user count: " + iCount);
				}

				Thread.sleep(300);
			}
			
			in.close();
			is.close();
		}
		catch (Exception e) {
			e.printStackTrace();
		}
	}

	private void UserDeleteFile(String sPath) {
		try {
			File file = new File(sPath);
			FileInputStream is = new FileInputStream(file);
			InputStreamReader isr = new InputStreamReader(is);
			BufferedReader in = new BufferedReader(isr);

			int iCount = 0;
			String sLine = null;
			while ((sLine = in.readLine()) != null) {
				String sLineTemp = sLine.trim();
				
				String sUser = "";
				String[] sSect = sLineTemp.split(" ", 2);
				if (sSect.length >= 1) {
					sUser = sSect[0].trim();
				}
				else {
					continue;
				}
				
				String sData = "65:(User){" + m_webClient.GetNode().omlEncode(sUser) + "}";
				int iReqID = m_webClient.Request(sData, "");
				if (iReqID < 0) {
					int iErr = -iReqID;
					OutString("   iErr: " + iErr);
				}
				else {
					m_webClient.GetResult(iReqID);
					iCount++;
					OutString("   Delete user count: " + iCount);
				}

				Thread.sleep(300);
			}
			
			in.close();
			is.close();
		}
		catch (Exception e) {
			e.printStackTrace();
		}
	}


	// main entry functions.
	public static void main(String sArg[]) {
		String sCfgPath = "";
		if (sArg.length > 0) {
			sCfgPath = sArg[0];
		}

		try {
			pgTunnelSvrTool oTool = new pgTunnelSvrTool();
			oTool.Run(sCfgPath);
		}
		catch (Exception ex) {
			OutString("pptun server tool run main failed: " + ex.toString());
		}
	}
}
