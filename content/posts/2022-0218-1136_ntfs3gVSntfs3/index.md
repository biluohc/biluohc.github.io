+++
title = "ntfs-3g 与 Linux 5.15+ ntfs3 驱动的简单性能测试"
slug = "NTFS3gVsNTFS3"
date = '2022-02-18 11:36:14+08:00'
#draft = true

[taxonomies]
categories = ["articles"]
tags = [ "linux", "ntfs3" ]
+++


Linux Kernel 5.15 合并了 Paragon 提供的 NTFS3 内核驱动， 拥有更高的性能和更多的特性

内核文档: [https://www.kernel.org/doc/html/latest/filesystems/ntfs3.html](https://www.kernel.org/doc/html/latest/filesystems/ntfs3.html)

驱动对比: [https://www.paragon-software.com/home/ntfs3-driver-faq/](https://www.paragon-software.com/home/ntfs3-driver-faq/)

## 系统信息

```sh
OS: openSUSE 20220126
Kernel: x86_64 Linux 5.16.2-1-default
```

##  通过 dd 命令在内存盘上做的测试

```sh
~/D/cache $ mkdir -p z                                                                                                              
~/D/cache $ dd if=/dev/zero of=out bs=1M count=5200                                                                                 
记录了5200+0 的读入
记录了5200+0 的写出
5452595200字节（5.5 GB，5.1 GiB）已复制，1.05791 s，5.2 GB/s
~/D/cache $ mkfs.ntfs -F out                                                                                               1s 363ms 
out is not a block device.
mkntfs forced anyway.
Initializing device with zeroes: 100% - Done.
Creating NTFS volume structures.
mkntfs completed successfully. Have a nice day.
~/D/cache $                                                                                                                2s 804ms
```

### ntfs-3g
```sh
~/D/cache $ sudo mount -t ntfs-3g out -o loop z                                                                                     
~/D/cache $ rm z/out                                                                                                                
~/D/cache $ dd if=/dev/zero of=z/out bs=1M count=4800                                                                               
记录了4800+0 的读入
记录了4800+0 的写出
5033164800字节（5.0 GB，4.7 GiB）已复制，16.5307 s，304 MB/s
~/D/cache $ dd if=/dev/zero of=z/out bs=1M count=4800                                                                     16s 550ms 
记录了4800+0 的读入
记录了4800+0 的写出
5033164800字节（5.0 GB，4.7 GiB）已复制，16.7989 s，300 MB/s
~/D/cache $ dd if=z/out of=/dev/null bs=1M                                                                                16s 934ms 
记录了4800+0 的读入
记录了4800+0 的写出
5033164800字节（5.0 GB，4.7 GiB）已复制，2.72367 s，1.8 GB/s
~/D/cache $ dd if=z/out of=/dev/null bs=1M                                                                                 2s 731ms 
记录了4800+0 的读入
记录了4800+0 的写出
5033164800字节（5.0 GB，4.7 GiB）已复制，2.80592 s，1.8 GB/s
~/D/cache $                                                                                                                2s 817ms
```

写入占用有一点高, 读取时还好:
```sh
 4424 root      20   0   10.5m   2.6m   1.9m R 88.24 0.008   0:18.63 mount.ntfs-3g                                                  
  160 root      20   0    0.0m   0.0m   0.0m S 27.94 0.000   0:52.20 kswapd0  
```

### ntfs3
```sh
~/D/cache $ sudo mount -t ntfs3 out -o loop z                                                                                 314ms 
~/D/cache $ rm z/out                                                                                                                
~/D/cache $ dd if=/dev/zero of=z/out bs=1M count=4800                                                                      1s 592ms 
记录了4800+0 的读入
记录了4800+0 的写出
5033164800字节（5.0 GB，4.7 GiB）已复制，1.98633 s，2.5 GB/s
~/D/cache $ dd if=/dev/zero of=z/out bs=1M count=4800                                                                      1s 996ms 
记录了4800+0 的读入
记录了4800+0 的写出
5033164800字节（5.0 GB，4.7 GiB）已复制，2.03256 s，2.5 GB/s
~/D/cache $ dd if=z/out of=/dev/null bs=1M                                                                                 2s 306ms 
记录了4800+0 的读入
记录了4800+0 的写出
5033164800字节（5.0 GB，4.7 GiB）已复制，1.73642 s，2.9 GB/s
~/D/cache $ dd if=z/out of=/dev/null bs=1M                                                                                 1s 739ms 
记录了4800+0 的读入
记录了4800+0 的写出
5033164800字节（5.0 GB，4.7 GiB）已复制，1.59989 s，3.1 GB/s
~/D/cache $                                                                                                                1s 609ms 
```

写入占用比 ntfs-3g 低一些:
```sh
30202 root      20   0    0.0m   0.0m   0.0m R 48.50 0.000   0:07.87 kworker/u32:1+loop0
  160 root      20   0    0.0m   0.0m   0.0m R 25.91 0.000   1:13.72 kswapd0     
```

## 总结

内核驱动开销变低, 读取性能有所提升，写入性能大幅提升，不考虑硬盘速度的话，写入速度接近10x
