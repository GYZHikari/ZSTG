#ifndef RESOURCE_H_INCLUDED
#define RESOURCE_H_INCLUDED
/**
 * �Ը�����Դ�Ķ��塣
 * @author ZHG <CyberZHG@gmail.com>
 */

/**
 * �Դ������ԵĶ��塣
 */
#define WINDOW_TITLE        "ZSTG 1 Memset"
#define WINDOW_WIDTH        800
#define WINDOW_HEIGHT       600
#define WINDOW_FULLSCREEN   false

/**
 * ��Ҫ���ص�����ͼƬ��
 */
enum ImageResouce
{
    RES_IMAGE_GAME_BACKGROUND,
    RES_IMAGE_BULLET,
    RES_IMAGE_LIVING
};
#define RES_IMAGE_PATH_GAME_BACKGROUND      "back.png"
#define RES_IMAGE_SIZE_GAME_BACKGROUND_W    800
#define RES_IMAGE_SIZE_GAME_BACKGROUND_H    600
#define RES_IMAGE_PATH_BULLET               "bullet.png"
#define RES_IMAGE_PATH_BULLET_W             1024
#define RES_IMAGE_PATH_BULLET_H             1024
#define RES_IMAGE_PATH_LIVING               "living.png"
#define RES_IMAGE_PATH_LIVING_W             1024
#define RES_IMAGE_PATH_LIVING_H             1024

/**
 * ͼ����ͼƬ�е�λ�á�
 */
#define RES_POS_GAME_BACKGROUND_LEFT_X      0
#define RES_POS_GAME_BACKGROUND_LEFT_Y      0
#define RES_POS_GAME_BACKGROUND_LEFT_W      50
#define RES_POS_GAME_BACKGROUND_LEFT_H      600

#define RES_POS_GAME_BACKGROUND_TOP_X       50
#define RES_POS_GAME_BACKGROUND_TOP_Y       0
#define RES_POS_GAME_BACKGROUND_TOP_W       550
#define RES_POS_GAME_BACKGROUND_TOP_H       50

#define RES_POS_GAME_BACKGROUND_BOTTOM_X    50
#define RES_POS_GAME_BACKGROUND_BOTTOM_Y    550
#define RES_POS_GAME_BACKGROUND_BOTTOM_W    550
#define RES_POS_GAME_BACKGROUND_BOTTOM_H    50

#define RES_POS_GAME_BACKGROUND_RIGHT_X     550
#define RES_POS_GAME_BACKGROUND_RIGHT_Y     0
#define RES_POS_GAME_BACKGROUND_RIGHT_W     250
#define RES_POS_GAME_BACKGROUND_RIGHT_H     600

#endif // RESOURCE_H_INCLUDED
