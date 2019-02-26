#include <Windows.h>
#include <wingdi.h>
#include <stdio.h>

#define BTN_EXIT            10001
#define BTN_WEBSITE         10002
#define BTN_GIT_DEMO        10003
#define BTN_CHANGE          20001

#define BTN_WIDTH          	160
#define BTN_HEIGHT          32
#define BTN_SPACING        	16

LRESULT CALLBACK WinSunProc(HWND hwnd,UINT uMsg,WPARAM wParam,LPARAM lParam);
int btnClicked = 0;

int WINAPI WinMain (HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nShowCmd)
{
    //���崰����
    WNDCLASS wndcls;
    //��������������ɹ��������ں󷵻صľ��
    HWND hwnd;
    //������Ϣ�ṹ�����
    MSG msg;

    //�ṹ��󸽼ӵ��ֽ�����һ����Ϊ0
    wndcls.cbClsExtra       = 0;
    //����ʵ�����ӵ��ֽ�����һ����Ϊ0
    wndcls.cbWndExtra       = 0;
    //������ɫ
    wndcls.hbrBackground    = (HBRUSH)CreateSolidBrush(RGB(242, 242, 242));
    //wndcls.hbrBackground    = (HBRUSH)GetStockObject(WHITE_BRUSH);
    //�����
    wndcls.hCursor          = LoadCursor(NULL,IDC_ARROW);
    //ͼ���� ��������ʾ��ͼ��
    wndcls.hIcon            = LoadIcon(NULL,IDI_APPLICATION);
    //ģ����
    wndcls.hInstance        = hInstance;
    //����ָ�룬ָ��������Ϣ�ĺ������
    wndcls.lpfnWndProc      = WinSunProc;
    //�Զ�����������Ҫ�����������ظ�
    wndcls.lpszClassName    = "windows";
    //�˵������ַ���
    wndcls.lpszMenuName     = NULL;
    //ָ�����ڷ�� ������� [#### ע��1 ####]
    wndcls.style            = CS_HREDRAW | CS_VREDRAW;

    //ע�ᴰ���࣬���ʧ��ֱ�ӷ���0��������
    if (!RegisterClass (&wndcls)) return 0;

    //��������
    hwnd = CreateWindowEx(
        WS_EX_WINDOWEDGE,
        "windows",
        "Demo win32api by civen.",
        WS_OVERLAPPEDWINDOW,
        (GetSystemMetrics(SM_CXSCREEN) - 800) / 2,
        (GetSystemMetrics(SM_CYSCREEN) - 600) / 2,
        800, // ���ڿ��
        600, // ���ڸ߶�
        NULL,
        NULL,
        hInstance,
        NULL);

    //APIWS_OVERLAPPEDWINDOWΪ Window Styles  //������� [#### ע��2 ####]

    //��ʾ�����API ������Ҫ��ʾ�Ĵ���������ʾ��ʽ
    ShowWindow(hwnd, SW_SHOWNORMAL);

    //ˢ�´����API
    UpdateWindow(hwnd);

    //������Ϣѭ��
    while(GetMessage(&msg,NULL,0,0))
    {
        //���������Ϣת��Ϊ�ַ���Ϣ���ַ���Ϣ���͵������̵߳���Ϣ�����У�����һ���̵߳��ú���GetMessage��PeekMessageʱ������
        TranslateMessage(&msg);

        //�ú�������һ����Ϣ�����ڳ���ͨ�����ȴ�GetMessageȡ�õ���Ϣ����Ϣ�����ȵ��Ĵ��ڳ�����MainProc()����
        DispatchMessage(&msg);
    }

    return 0;
}


LRESULT CALLBACK WinSunProc(HWND hwnd,UINT uMsg,WPARAM wParam,LPARAM lParam)//�ص���������
{
    switch(uMsg)
    {
        //�رմ�����ϵͳ���͵���Ϣ
        case WM_DESTROY:
            //�����˳���ϢGetMessage�յ���Ϣ��return 0,�������˳���Ϣѭ��
            PostQuitMessage(0);
            break;
        case WM_CREATE:
            {
                CreateWindow(
                    "BUTTON",
                    "Rsume",
                    WS_VISIBLE | WS_CHILD | BS_PUSHBUTTON,
                    80,
					(BTN_HEIGHT + BTN_SPACING) * 0 + BTN_SPACING,
					BTN_WIDTH,
					BTN_HEIGHT,
                    hwnd,
                    (HMENU) BTN_WEBSITE,
                    ((LPCREATESTRUCT)lParam)->hInstance,
                    NULL);
                CreateWindow(
                    "BUTTON",
                    "Demo",
                    WS_VISIBLE | WS_CHILD | BS_PUSHBUTTON,
                    80,
					(BTN_HEIGHT + BTN_SPACING) * 1 + BTN_SPACING,
					BTN_WIDTH,
					BTN_HEIGHT,
                    hwnd,
                    (HMENU) BTN_GIT_DEMO,
                    ((LPCREATESTRUCT)lParam)->hInstance,
                    NULL);
                CreateWindow(
                    "BUTTON",
                    "Test",
                    WS_VISIBLE | WS_CHILD | BS_PUSHBUTTON,
                    80,
					(BTN_HEIGHT + BTN_SPACING) * 2 + BTN_SPACING,
					BTN_WIDTH,
					BTN_HEIGHT,
                    hwnd,
                    (HMENU) BTN_CHANGE,
                    ((LPCREATESTRUCT)lParam)->hInstance,
                    NULL);
                CreateWindow(
                    "BUTTON",
                    "�˳�",
                    WS_VISIBLE | WS_CHILD | BS_PUSHBUTTON,
                    80,
					(BTN_HEIGHT + BTN_SPACING) * 3 + BTN_SPACING,
					BTN_WIDTH,
					BTN_HEIGHT,
                    hwnd,
                    (HMENU) BTN_EXIT,
                    ((LPCREATESTRUCT)lParam)->hInstance,
                    NULL);
                break;
            }
        case WM_COMMAND:
            switch(LOWORD(wParam))
            {
                case BTN_WEBSITE:
                    ShellExecute(NULL, "open", "https://civenz.github.io/", NULL, NULL, SW_SHOWNORMAL);
                    break;
                case BTN_GIT_DEMO:
                    ShellExecute(NULL, "open", "https://github.com/civenz/demo/", NULL, NULL, SW_SHOWNORMAL);
                    break;
                case BTN_CHANGE:
                    if(btnClicked == 0) {
						btnClicked = 1;
                        SendMessage((HWND)lParam, WM_SETTEXT, (WPARAM)NULL, (LPARAM) "Civen");
                    } else {
						btnClicked = 0;
						SendMessage((HWND)lParam, WM_SETTEXT, (WPARAM)NULL, (LPARAM) "Hi");
					}
                    break;
                case BTN_EXIT:
                    PostQuitMessage(0);
                    break;
                default:
                    break;
            }
        default:
            //���������Ϣ����ϵͳ����
            return DefWindowProc(hwnd,uMsg,wParam,lParam);
    }
    return 0;
}