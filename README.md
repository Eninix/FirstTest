# 测试及学习Git的Test

---

## 基础指令

1. git config --global user.name "用户名"
2. git config --global user.email "邮箱"
3. git init (初始化一个仓库)
4. git add (将文件添加到缓存区)
5. git commit -m "注释"
6. git status (查看项目的当前状态)
7. git log (查看当前版本及以前版本的日志,可获取版本号)
8. git log --pretty=oneline (同上,但每个版本单行显示)
9. git reset --hard 版本号 (回到曾经的版本)
10. git reflog (查看历史日志,可获取版本号)
11. git clone (后接https地址,可以克隆仓库)
12. git push (上传至线上仓库)
13. git pull (从线上仓库同步)

## 分支相关指令

14. git branch (查看分支)
15. git branch 分支名 (创建分支)
16. git checkout 分支名 (切换分支)
17. git branch -d 分支名 (删除分支)
18. git merge 需要被分支名 (合并分支)