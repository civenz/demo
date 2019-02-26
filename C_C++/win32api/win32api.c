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
    //定义窗体类
    WNDCLASS wndcls;
    //定义句柄用来保存成功创建窗口后返回的句柄
    HWND hwnd;
    //定义消息结构体变量
    MSG msg;

    //结构体后附加的字节数，一般总为0
    wndcls.cbClsExtra       = 0;
    //窗体实例附加的字节数，一般总为0
    wndcls.cbWndExtra       = 0;
    //背景颜色
    wndcls.hbrBackground    = (HBRUSH)CreateSolidBrush(RGB(242, 242, 242));
    //wndcls.hbrBackground    = (HBRUSH)GetStockObject(WHITE_BRUSH);
    //光标句柄
    wndcls.hCursor          = LoadCursor(NULL,IDC_ARROW);
    //图标句柄 任务栏显示的图标
    wndcls.hIcon            = LoadIcon(NULL,IDI_APPLICATION);
    //模块句柄
    wndcls.hInstance        = hInstance;
    //函数指针，指向处理窗口消息的函数入口
    wndcls.lpfnWndProc      = WinSunProc;
    //自定义类名，不要与其他类名重复
    wndcls.lpszClassName    = "windows";
    //菜单名的字符串
    wndcls.lpszMenuName     = NULL;
    //指定窗口风格 详见参数 [#### 注释1 ####]
    wndcls.style            = CS_HREDRAW | CS_VREDRAW;

    //注册窗体类，如果失败直接返回0结束程序
    if (!RegisterClass (&wndcls)) return 0;

    //创建窗体
    hwnd = CreateWindowEx(
        WS_EX_WINDOWEDGE,
        "windows",
        "Demo win32api by civen.",
        WS_OVERLAPPEDWINDOW,
        (GetSystemMetrics(SM_CXSCREEN) - 800) / 2,
        (GetSystemMetrics(SM_CYSCREEN) - 600) / 2,
        800, // 窗口宽度
        600, // 窗口高度
        NULL,
        NULL,
        hInstance,
        NULL);

    //APIWS_OVERLAPPEDWINDOW为 Window Styles  //详见参数 [#### 注释2 ####]

    //显示窗体的API 传入需要显示的窗体句柄和显示方式
    ShowWindow(hwnd, SW_SHOWNORMAL);

    //刷新窗体的API
    UpdateWindow(hwnd);

    //进入消息循环
    while(GetMessage(&msg,NULL,0,0))
    {
        //将虚拟键消息转换为字符消息。字符消息被送到调用线程的消息队列中，在下一次线程调用函数GetMessage或PeekMessage时被读出
        TranslateMessage(&msg);

        //该函数调度一个消息给窗口程序。通常调度从GetMessage取得的消息。消息被调度到的窗口程序即是MainProc()函数
        DispatchMessage(&msg);
    }

    return 0;
}


LRESULT CALLBACK WinSunProc(HWND hwnd,UINT uMsg,WPARAM wParam,LPARAM lParam)//回调函数定义
{
    switch(uMsg)
    {
        //关闭窗口是系统发送的消息
        case WM_DESTROY:
            //发送退出消息GetMessage收到消息后将return 0,主函数退出消息循环
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
                    "退出",
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
            //不处理的消息交给系统处理。
            return DefWindowProc(hwnd,uMsg,wParam,lParam);
    }
    return 0;
}