Þ    ¯        é         °     ±  ?   È  K     K   T  C      ;   ä  C      w   d  9   Ü       G        à  @   s  N   ´               6     R     j  J   ~  9   É  4     2   8  @   k  R   ¬  >   ÿ     >     N     T  0   t  	   ¥  j   ¯  _     ,   z  3   §  &   Û            P   £  Q   ô  c   F  Ì   ª  -   w     ¥     Ã  @   à  /   !  :   Q              '   Á     é  "   	     ,  $   J     o  #        ³  1   Ò  *        /  $   M  K   r  +   ¾  /   ê  7     +   R  !   ~  (      +   É  2   õ     (  ,   E  #   r  #     :   º  "   õ  &     !   ?     a  (   ~  0   §  %   Ø  #   þ     "   '   A   (   i         !   ²   &   Ô      û      !     7!     T!  1   m!  8   !     Ø!  &   õ!  ,   "     I"      g"  /   "  .   ¸"  -   ç"  -   #     C#  ;   K#     #  5   #  ;   Å#  (   $     *$  +   G$  %   s$     $     ®$      Ë$  3   ì$  6    %  1   W%     %  '   ¨%  ;   Ð%  _   &     l&  R   &  8   Ò&  4   '  ?   @'     '     '  !   '  F   ¿'  2   (     9(     O(     h(  "   (  .   ¤(  #   Ó(  ,   ÷(  0   $)  =   U)  5   )  2   É)  5   ü)  /   2*     b*  *   |*  %   §*     Í*      ë*  '   +  H   4+  $   }+  /   ¢+  &   Ò+     ù+  ,   ,  I   B,  1   ,  <   ¾,  @   û,  6   <-  4   s-  4   ¨-      Ý-  6   þ-  .   5.  5   d.  1   .  -   Ì.  8   ú.  	   3/  º  =/  -   ø0  N   &1  i   u1  N   ß1  <   .2  E   k2  Q   ±2  c   3  ?   g3  ¥   §3  K   M4  ´   4  E   N5     5  .   #6  2   R6  7   6  &   ½6     ä6  W   7  T   Y7  U   ®7  p   8  j   u8     à8  n   j9     Ù9     ê9  5   ò9  N   (:     w:  «   :  ·   5;  ;   í;  ^   )<  3   <  (   ¼<  ã   å<     É=     Y>     ö>  c  ?  L   å@  ?   2A  !   rA  l   A  ?   B  T   AB     B  $   µB  B   ÚB  0   C  A   NC  ;   C  J   ÌC  .   D  ;   FD  5   D  Q   ¸D  G   
E  @   RE  G   E  u   ÛE  >   QF  B   F  `   ÓF  O   4G  A   G  M   ÆG  S   H  b   hH  ;   ËH  W   I  S   _I  J   ³I  A   þI  8   @J  <   yJ  ;   ¶J  8   òJ  q   +K  D   K  >   âK  ;   !L  5   ]L  D   L  L   ØL  8   %M  L   ^M  G   «M  9   óM  4   -N  :   bN  .   N  A   ÌN  X   O  0   gO  I   O  B   âO  5   %P  5   [P  E   P  R   ×P  >   *Q  >   iQ     ¨Q  g   ´Q     R  O   1R  b   R  G   äR  1   ,S  ?   ^S  4   S     ÓS  *   ïS  .   T  [   IT  _   ¥T  j   U  2   pU  =   £U  h   áU     JV  $   ÐV  _   õV  R   UW  Y   ¨W  O   X     RX     hX  "   X  o   ¢X  q   Y  0   Y  9   µY  ?   ïY  4   /Z  N   dZ  /   ³Z  =   ãZ  K   ![  p   m[  R   Þ[  W   1\  Z   \  o   ä\  *   T]  H   ]  =   È]  B   ^  +   I^  c   u^     Ù^  /   c_  =   _  4   Ñ_  '   `  :   .`  a   i`  ;   Ë`  I   a  p   Qa  b   Âa  E   %b  H   kb  *   ´b  Q   ßb  E   1c  L   wc  C   Äc  :   d  :   Cd     ~d     p                ¦   ;       ª   7   r   -         s   i   f   ]           ¯           \   3   
      ¥         N   u   ®   2   8          m           ¨             %   !   J                 0       9                  4   W           *       @          D   <   e   )   {       I   g      «   5      ­       w      x   6   £                           }   H          ?                 ¤   v          T          b   k   y      n   K      l   ~   _   E           S             Q   Y       [             &   =            a   #         G   ,      §   .            	      t   V         1                 ¬   (   '              L           $   c          M   h      ¢      o       +      /       B       >               ¡   q      Z   |   F   P       ^   z      R                          :   X   j   U          "         ©       `       A             O   C          d        
Report bugs to <%s>.
       --debug                    write a lot of debug messages
       --no-ensure-shutdown       do not automatically fix unclean shutdown
       --source-pgdata=DIRECTORY  source data directory to synchronize with
       --source-server=CONNSTR    source server to synchronize with
   -?, --help                     show this help, then exit
   -D, --target-pgdata=DIRECTORY  existing data directory to modify
   -N, --no-sync                  do not wait for changes to be written
                                 safely to disk
   -P, --progress                 write progress messages
   -R, --write-recovery-conf      write configuration for replication
                                 (requires --source-server)
   -V, --version                  output version information, then exit
   -c, --restore-target-wal       use restore_command in target configuration to
                                 retrieve WAL files from archives
   -n, --dry-run                  stop before modifying anything
 "%s" is a symbolic link, but symbolic links are not supported on this platform "%s" is not a directory "%s" is not a regular file "%s" is not a symbolic link %*s/%s kB (%d%%) copied %s home page: <%s>
 %s resynchronizes a PostgreSQL cluster with another copy of the cluster.

 BKPBLOCK_HAS_DATA not set, but data length is %u at %X/%X BKPBLOCK_HAS_DATA set, but no data included at %X/%X BKPBLOCK_SAME_REL set but no previous rel at %X/%X BKPIMAGE_HAS_HOLE not set, but hole offset %u length %u at %X/%X BKPIMAGE_HAS_HOLE set, but hole offset %u length %u block image length %u at %X/%X BKPIMAGE_IS_COMPRESSED set, but block image length %u at %X/%X Command was: %s Done! Expected a numeric timeline ID. Expected a write-ahead log switchpoint location. Options:
 The program "%s" is needed by %s but was not found in the
same directory as "%s".
Check your installation. The program "%s" was found by "%s"
but was not the same version as %s.
Check your installation. Timeline IDs must be in increasing sequence. Timeline IDs must be less than child timeline's ID. Try "%s --help" for more information.
 Usage:
  %s [OPTION]...

 WAL file is from different database system: WAL file database system identifier is %llu, pg_control database system identifier is %llu WAL file is from different database system: incorrect XLOG_BLCKSZ in page header WAL file is from different database system: incorrect segment size in page header WAL record modifies a relation, but record type is not recognized: lsn: %X/%X, rmgr: %s, info: %02X WAL segment size must be a power of two between 1 MB and 1 GB, but the control file specifies %d byte WAL segment size must be a power of two between 1 MB and 1 GB, but the control file specifies %d bytes You must run %s as the PostgreSQL superuser.
 backup label buffer too small cannot be executed by "root" cannot create restricted tokens on this platform: error code %lu cannot duplicate null pointer (internal error)
 clusters are not compatible with this version of pg_rewind connected to server contrecord is requested by %X/%X could not allocate SIDs: error code %lu could not clear search_path: %s could not close directory "%s": %m could not close file "%s": %m could not close target file "%s": %m could not connect to server: %s could not create directory "%s": %m could not create file "%s": %m could not create restricted token: error code %lu could not create symbolic link at "%s": %m could not fetch file list: %s could not fetch remote file "%s": %s could not find common ancestor of the source and target cluster's timelines could not find previous WAL record at %X/%X could not find previous WAL record at %X/%X: %s could not get exit code from subprocess: error code %lu could not load library "%s": error code %lu could not open directory "%s": %m could not open file "%s" for reading: %m could not open file "%s" for truncation: %m could not open file "%s" restored from archive: %m could not open file "%s": %m could not open process token: error code %lu could not open source file "%s": %m could not open target file "%s": %m could not re-execute with restricted token: error code %lu could not read WAL record at %X/%X could not read WAL record at %X/%X: %s could not read directory "%s": %m could not read file "%s": %m could not read file "%s": read %d of %zu could not read permissions of directory "%s": %m could not read symbolic link "%s": %m could not remove directory "%s": %m could not remove file "%s": %m could not remove symbolic link "%s": %m could not restore file "%s" from archive could not seek in file "%s": %m could not seek in source file: %m could not seek in target file "%s": %m could not send COPY data: %s could not send end-of-COPY: %s could not send file list: %s could not send query: %s could not set libpq connection to single row mode could not start process for command "%s": error code %lu could not stat file "%s": %m could not truncate file "%s" to %u: %m could not use restore_command with %%r alias could not write file "%s": %m could not write to file "%s": %m creating backup label and updating control file data file "%s" in source is not a regular file error running query (%s) in source server: %s error running query (%s) on source server: %s error:  executing "%s" for target server to complete crash recovery fatal:  full_page_writes must be enabled in the source server incorrect resource manager data checksum in record at %X/%X invalid action (CREATE) for regular file invalid block_id %u at %X/%X invalid compressed image at %X/%X, block %d invalid contrecord length %u at %X/%X invalid control file invalid data in history file invalid data in history file: %s invalid info bits %04X in log segment %s, offset %u invalid magic number %04X in log segment %s, offset %u invalid record length at %X/%X: wanted %u, got %u invalid record offset at %X/%X invalid resource manager ID %u at %X/%X need to copy %lu MB (total source directory size is %lu MB) neither BKPIMAGE_HAS_HOLE nor BKPIMAGE_IS_COMPRESSED set, but block image length is %u at %X/%X no rewind required no source server information (--source-server) specified for --write-recovery-conf no source specified (--source-pgdata or --source-server) no target data directory specified (--target-pgdata) only one of --source-pgdata or --source-server can be specified out of memory out of memory
 out-of-order block_id %u at %X/%X out-of-sequence timeline ID %u (after %u) in log segment %s, offset %u postgres single-user mode in target cluster failed reading WAL in target reading source file list reading target file list record length %u at %X/%X too long record with incorrect prev-link %X/%X at %X/%X record with invalid length at %X/%X restore_command failed due to the signal: %s restore_command is not set in the target cluster rewinding from last common checkpoint at %X/%X on timeline %u servers diverged at WAL location %X/%X on timeline %u source and target cluster are on the same timeline source and target clusters are from different systems source data directory must be shut down cleanly source file list is empty source server must not be in recovery mode symbolic link "%s" target is too long syncing target data directory syntax error in history file: %s target server must be shut down cleanly target server needs to use either data checksums or "wal_log_hints = on" there is no contrecord flag at %X/%X too many command-line arguments (first is "%s") unexpected EOF while reading file "%s" unexpected control file CRC unexpected control file size %d, expected %d unexpected data types in result set while fetching remote files: %u %u %u unexpected file size for "%s": %lu instead of %lu unexpected null values in result while fetching remote files unexpected page modification for directory or symbolic link "%s" unexpected pageaddr %X/%X in log segment %s, offset %u unexpected result format while fetching remote files unexpected result length while fetching remote files unexpected result set from query unexpected result set size while fetching remote files unexpected result set while fetching file list unexpected result set while fetching remote file "%s" unexpected result while fetching remote files: %s unexpected result while sending file list: %s unrecognized result "%s" for current WAL insert location warning:  Project-Id-Version: pg_rewind (PostgreSQL 13)
Report-Msgid-Bugs-To: pgsql-bugs@lists.postgresql.org
PO-Revision-Date: 2020-08-21 23:25+0900
Last-Translator: Kyotaro Horiguchi <horikyota.ntt@gmail.com>
Language-Team: Japan PostgreSQL Users Group <jpug-doc@ml.postgresql.jp>
Language: ja
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
X-Generator: Poedit 1.8.13
Plural-Forms: nplurals=2; plural=n!=1;
 
ãã°ã¯<%s>ã«å ±åãã¦ãã ããã
       --debug                   å¤éã®ãããã°ã¡ãã»ã¼ã¸ãåºå
       --no-ensure-shutdown      éã¯ãªã¼ã³ã·ã£ãããã¦ã³å¾ã®ä¿®æ­£ãèªåã§è¡ããªã
       --source-pgdata=DIRECTORY åæåã¨ãããã¼ã¿ãã£ã¬ã¯ããª
       --source-server=CONNSTR   åæåã¨ãããµã¼ã
   -?, --help                    ãã®ãã«ããè¡¨ç¤ºãã¦çµäº
   -D, --target-pgdata=DIRECTORY ä¿®æ­£ãè¡ãæ¢å­ãã¼ã¿ãã£ã¬ã¯ããª
   -N, --no-sync                 å¤æ´ã®ãã£ã¹ã¯ã¸ã®å®å¨ãªæ¸ãåºããå¾æ©ããªã
   -P, --progress                é²æã¡ãã»ã¼ã¸ãåºå
   -R, --write-recovery-conf     ã¬ããªã±ã¼ã·ã§ã³ã®ããã®è¨­å®ãæ¸ãè¾¼ã
                                (--source-server ãå¿è¦ã¨ãªãã¾ã)
   -V, --version                 ãã¼ã¸ã§ã³æå ±ãè¡¨ç¤ºãã¦çµäº
   -c, --restore-target-wal      ã¿ã¼ã²ããã®è¨­å®ã®ä¸­ã®restore_commandãä½¿ç¨ãã¦
                                ã¢ã¼ã«ã¤ãããWALãã¡ã¤ã«ãåå¾ãã
   -n, --dry-run                 ä¿®æ­£ãå§ããåã«åæ­¢ãã
 "%s"ã¯ã·ã³ããªãã¯ãªã³ã¯ã§ããããã®ãã©ãããã©ã¼ã ã§ã¯ã·ã³ããªãã¯ãªã³ã¯ããµãã¼ããã¦ãã¾ãã "%s"ã¯ãã£ã¬ã¯ããªã§ã¯ããã¾ãã "%s" ã¯éå¸¸ã®ãã¡ã¤ã«ã§ã¯ããã¾ãã "%s"ã¯ã·ã³ããªãã¯ãªã³ã¯ã§ã¯ããã¾ãã %*s/%s kB (%d%%) ã³ãã¼ãã¾ãã %s ãã¼ã ãã¼ã¸: <%s>
 %s ã¯PostgreSQLã¯ã©ã¹ã¿ããã®ã¯ã©ã¹ã¿ã®ã³ãã¼ã§ååæãã¾ãã

 BKPBLOCK_HAS_DATAãè¨­å®ããã¦ãã¾ãããã%2$X/%3$Xã®ãã¼ã¿é·ã¯%1$u BKPBLOCK_HAS_DATAãè¨­å®ããã¦ãã¾ããã%X/%Xã«ãã¼ã¿ãããã¾ãã BKPBLOCK_SAME_RELãè¨­å®ããã¦ãã¾ããã%X/%Xã«ããã¦ä»¥åã®ãªã¬ã¼ã·ã§ã³ãããã¾ãã BKPIMAGE_HAS_HOLEãè¨­å®ããã¦ãã¾ãããã%3$X/%4$Xã«ãã¼ã«ãªãã»ãã%1$uãé·ã%2$u BKPIMAGE_HAS_HOLEãè¨­å®ããã¦ãã¾ããã%4$X/%5$Xã§ãã¼ã«ãªãã»ãã%1$uãé·ã%2$uããã­ãã¯ã¤ã¡ã¼ã¸é·%3$u BKPIMAGE_IS_COMPRESSEDãè¨­å®ããã¦ãã¾ããã%2$X/%3$Xã«ããã¦ãã­ãã¯ã¤ã¡ã¼ã¸é·ã%1$u ã³ãã³ã: %s å®äº! æ°å­ã®ã¿ã¤ã ã©ã¤ã³IDãæ³å®ãã¾ããã åè¡æ¸ãè¾¼ã¿ã­ã°ã®åãæ¿ãç¹ã®å ´æãããã¯ãã§ããã ãªãã·ã§ã³:
 %2$sã«ã¯"%1$s"ãã­ã°ã©ã ãå¿è¦ã§ããã"%3$s"ã¨åããã£ã¬ã¯ããª
ã«ããã¾ããã§ããã
ã¤ã³ã¹ãã¼ã«ç¶æ³ãç¢ºèªãã¦ãã ããã "%2$s"ããã­ã°ã©ã "%1$s"ãè¦ã¤ãã¾ããããããã¯%3$sã¨åã
ãã¼ã¸ã§ã³ã§ã¯ããã¾ããã§ããã
ã¤ã³ã¹ãã¼ã«ç¶æ³ãç¢ºèªãã¦ãã ããã ã¿ã¤ã ã©ã¤ã³IDã¯æé ã§ãªããã°ãªãã¾ãã ã¿ã¤ã ã©ã¤ã³IDã¯å­ã®ã¿ã¤ã ã©ã¤ã³IDããå°ãããªããã°ãªãã¾ããã è©³ç´°ã¯"%s --help"ãå®è¡ãã¦ãã ããã
 ä½¿ç¨æ¹æ³:
 %s [ãªãã·ã§ã³]...

 WALãã¡ã¤ã«ã¯ç°ãªããã¼ã¿ãã¼ã¹ã·ã¹ãã ç±æ¥ã®ãã®ã§ã: WALãã¡ã¤ã«ã®ãã¼ã¿ãã¼ã¹ã·ã¹ãã è­å¥å­ã¯ %lluã§ãpg_control ã«ããããã¼ã¿ãã¼ã¹ã·ã¹ãã è­å¥å­ã¯ %lluã§ã WAL ãã¡ã¤ã«ã¯ç°ãªããã¼ã¿ãã¼ã¹ã·ã¹ãã ç±æ¥ã®ãã®ã§ã: ãã¼ã¸ãããã¼ã®XLOG_BLCKSZãæ­£ããããã¾ãã WAL ãã¡ã¤ã«ã¯ç°ãªããã¼ã¿ãã¼ã¹ã·ã¹ãã ç±æ¥ã®ãã®ã§ã: ãã¼ã¸ãããã¼ã®ã»ã°ã¡ã³ããµã¤ãºãæ­£ããããã¾ãã WALã¬ã³ã¼ãã¯ãªã¬ã¼ã·ã§ã³ãä¿®æ­£ãã¾ãããã¬ã³ã¼ãã®åãèªè­ã§ãã¾ãã: lsn: %X/%Xãrmgr: %sãinfo: %02X WALã»ã°ã¡ã³ãã®ãµã¤ãºæå®ã¯1MBã¨1GBã®éã®2ã®ç´¯ä¹ã§ãªããã°ãªãã¾ããããããã³ã³ãã­ã¼ã«ãã¡ã¤ã«ã§ã¯%dãã¤ãã¨ãªã£ã¦ãã¾ã WALã»ã°ã¡ã³ãã®ãµã¤ãºæå®ã¯1MBã¨1GBã®éã®2ã®ç´¯ä¹ã§ãªããã°ãªãã¾ããããããã³ã³ãã­ã¼ã«ãã¡ã¤ã«ã§ã¯%dãã¤ãã¨ãªã£ã¦ãã¾ã PostgreSQLã®ã¹ã¼ãã¦ã¼ã¶ã§%sãå®è¡ããªããã°ãªãã¾ãã
 ããã¯ã¢ããã©ãã«ã®ãããã¡ãå°ãããã¾ã "root"ã§ã¯å®è¡ã§ãã¾ãã ãã®ãã©ãããã©ã¼ã ã§ã¯å¶éä»ããã¼ã¯ã³ãçæã§ãã¾ãã: ã¨ã©ã¼ã³ã¼ã %lu null ãã¤ã³ã¿ãè¤è£½ã§ãã¾ããï¼åé¨ã¨ã©ã¼ï¼
 ã¯ã©ã¹ã¿ã¯ããã®ãã¼ã¸ã§ã³ã®pg_rewindã¨ã®äºææ§ãããã¾ãã ãµã¼ãã¸æ¥ç¶ãã¾ãã %X/%Xã§ã¯contrecordãå¿è¦ã§ã SIDãå²ãå½ã¦ããã¾ããã§ãã: ã¨ã©ã¼ã³ã¼ã %lu search_pathãæ¶å»ã§ãã¾ããã§ãã: %s ãã£ã¬ã¯ããª"%s"ãã¯ã­ã¼ãºã§ãã¾ããã§ãã: %m ãã¡ã¤ã«"%s"ãã¯ã­ã¼ãºã§ãã¾ããã§ãã: %m ã¿ã¼ã²ãããã¡ã¤ã«"%s"ãã¯ã­ã¼ãºã§ãã¾ããã§ãã: %m ãµã¼ãã«æ¥ç¶ã§ãã¾ããã§ãã: %s ãã£ã¬ã¯ããª"%s"ãä½æã§ãã¾ããã§ãã: %m ãã¡ã¤ã«"%s"ãä½æã§ãã¾ããã§ãã: %m å¶éä»ããã¼ã¯ã³ãä½æã§ãã¾ããã§ãã: ã¨ã©ã¼ã³ã¼ã %lu "%s"ã«ã·ã³ããªãã¯ãªã³ã¯ãä½æã§ãã¾ããã§ãã: %m ãã¡ã¤ã«ãªã¹ãããã§ããã§ãã¾ããã§ãã: %s ãªã¢ã¼ããã¡ã¤ã«"%s"ããã§ããã§ãã¾ããã§ãã: %s ã½ã¼ã¹ã¯ã©ã¹ã¿ã¨ã¿ã¼ã²ããã¯ã©ã¹ã¿ã®ã¿ã¤ã ã©ã¤ã³ã®å±éã®ç¥åãè¦ã¤ãããã¾ãã %X/%Xã®åã®WALã¬ã³ã¼ããè¦ã¤ããã¾ããã§ãã %X/%Xã®åã®WALã¬ã³ã¼ããè¦ã¤ããã¾ããã§ãã: %s ãµããã­ã»ã¹ã®çµäºã³ã¼ããåå¾ã§ãã¾ããã§ããã: ã¨ã©ã¼ã³ã¼ã %lu ã©ã¤ãã©ãª"%s"ãã­ã¼ãã§ãã¾ããã§ãã: ã¨ã©ã¼ã³ã¼ã %lu ãã£ã¬ã¯ããª"%s"ããªã¼ãã³ã§ãã¾ããã§ãã: %m ãã¡ã¤ã«"%s"ãèª­ã¿åãç¨ã«ãªã¼ãã³ã§ãã¾ããã§ãã: %m ãã¡ã¤ã«"%s"ãåãè©°ãã®ããã«ãªã¼ãã³ã§ãã¾ããã§ãã: %m ã¢ã¼ã«ã¤ããããªã¹ãã¢ããããã¡ã¤ã«"%s"ã®ãªã¼ãã³ã«å¤±æãã¾ãã: %m ãã¡ã¤ã«"%s"ããªã¼ãã³ã§ãã¾ããã§ãã: %m ãã­ã»ã¹ãã¼ã¯ã³ããªã¼ãã³ã§ãã¾ããã§ãã: ã¨ã©ã¼ã³ã¼ã %lu ã½ã¼ã¹ãã¡ã¤ã«"%s"ããªã¼ãã³ãããã¨ãã§ãã¾ããã§ãã: %m ã¿ã¼ã²ãããã¡ã¤ã«"%s"ããªã¼ãã³ã§ãã¾ããã§ãã: %m å¶éä»ããã¼ã¯ã³ã§åå®è¡ã§ãã¾ããã§ãã: %lu %X/%Xã®WALã¬ã³ã¼ããèª­ã¿åãã¾ããã§ãã %X/%Xã®WALã¬ã³ã¼ããèª­ã¿åãã¾ããã§ãã: %s ãã£ã¬ã¯ããª"%s"ãèª­ã¿åãã¾ããã§ãã: %m ãã¡ã¤ã«"%s"ã®èª­ã¿åãã«å¤±æãã¾ãã: %m ãã¡ã¤ã«"%1$s"ãèª­ã¿è¾¼ãã¾ããã§ãã: %3$zuãã¤ãã®ãã¡%2$dãã¤ããèª­ã¿è¾¼ã¿ã¾ãã ãã£ã¬ã¯ããª"%s"ã®æ¨©éãèª­ã¿åãã¾ããã§ãã: %m ã·ã³ããªãã¯ãªã³ã¯"%s"ãèª­ãã¾ããã§ãã: %m ãã£ã¬ã¯ããª"%s"ãåé¤ã§ãã¾ããã§ãã: %m ãã¡ã¤ã«"%s"ãåé¤ã§ãã¾ããã§ãã: %m ã·ã³ããªãã¯ãªã³ã¯"%s"ãåé¤ã§ãã¾ããã§ãã: %m ãã¡ã¤ã«"%s"ãã¢ã¼ã«ã¤ããããªã¹ãã¢ã§ãã¾ããã§ãã ãã¡ã¤ã«"%s"ãã·ã¼ã¯ã§ãã¾ããã§ãã: %m ã½ã¼ã¹ãã¡ã¤ã«ãã·ã¼ã¯ãããã¨ãã§ãã¾ããã§ãã: %m ã¿ã¼ã²ãããã¡ã¤ã«"%s"ãã·ã¼ã¯ã§ãã¾ããã§ãã: %m COPY å¯¾è±¡ãã¼ã¿ãéä¿¡ã§ãã¾ããã§ãã: %s ã³ãã¼çµç«¯ãéä¿¡ã§ãã¾ããã§ãã: %s ãã¡ã¤ã«ãªã¹ããéä¿¡ã§ãã¾ããã§ãã: %s ã¯ã¨ãªãéä¿¡ã§ãã¾ããã§ãã: %s libpqæ¥ç¶ãåä¸è¡ã¢ã¼ãã«è¨­å®ã§ãã¾ããã§ãã "%s"ã³ãã³ãã®ãã­ã»ã¹ãèµ·åã§ãã¾ããã§ãã: ã¨ã©ã¼ã³ã¼ã %lu ãã¡ã¤ã«"%s"ã®statã«å¤±æãã¾ãã: %m ãã¡ã¤ã«"%s"ã%uãã¤ãã«åãè©°ãããã¾ããã§ãã: %m %%rã¨ã¤ãªã¢ã¹ãå«ãrestore_commandã¯ä½¿ç¨ã§ãã¾ãã ãã¡ã¤ã«"%s"ãæ¸ãåºãã¾ããã§ãã: %m ãã¡ã¤ã«"%s"ãæ¸ãåºãã¾ããã§ãã: %m backup labelãä½æãã¦å¶å¾¡ãã¡ã¤ã«ãæ´æ°ãã¦ãã¾ã ã½ã¼ã¹ã®ãã¼ã¿ãã¡ã¤ã«"%s"ã¯éå¸¸ã®ãã¡ã¤ã«ã§ã¯ããã¾ãã ã½ã¼ã¹ãµã¼ãã®å®è¡ä¸­ã®ã¯ã¨ãª(%s)ã§ã¨ã©ã¼: %s ã½ã¼ã¹ãµã¼ãã§å®è¡ä¸­ã®ã¯ã¨ãª(%s)ã§ã¨ã©ã¼: %s ã¨ã©ã¼:  ã¿ã¼ã²ãããµã¼ãã«å¯¾ãã¦"%s"ãå®è¡ãã¦ã¯ã©ãã·ã¥ãªã«ããªãå®äºããã¾ã è´å½çã¨ã©ã¼:  ã½ã¼ã¹ãµã¼ãã§ã¯full_pate_writesã¯æå¹ã§ãªããã°ãªãã¾ãã %X/%Xã®ã¬ã³ã¼ãåã®ãªã½ã¼ã¹ããã¼ã¸ã£ãã¼ã¿ã®ãã§ãã¯ãµã ãä¸æ­£ã§ã éå¸¸ã®ãã¡ã¤ã«ã«å¯¾ããä¸æ­£ãªã¢ã¯ã·ã§ã³(CREATE)ã§ã %2$X/%3$Xã«ãããblock_id %1$uãç¡å¹ã§ã %X/%Xããã­ãã¯ %d ã§ã®å§ç¸®ã¤ã¡ã¼ã¸ãç¡å¹ã§ã %2$X/%3$Xã®contrecordã®é·ã %1$u ãç¡å¹ã§ã ä¸æ­£ãªå¶å¾¡ãã¡ã¤ã« å±¥æ­´ãã¡ã¤ã«åã®ç¡å¹ãªãã¼ã¿ å±¥æ­´ãã¡ã¤ã«åã®ä¸æ­£ãªãã¼ã¿: %s ã­ã°ã»ã°ã¡ã³ã %2$sããªãã»ãã %3$u ã®æå ±ããã %1$04X ã¯ç¡å¹ã§ã ã­ã°ã»ã°ã¡ã³ã%2$sããªãã»ãã%3$uã®ãã¸ãã¯ãã³ãã¼%1$04Xã¯ç¡å¹ã§ã %X/%Xã®ã¬ã³ã¼ãé·ãç¡å¹ã§ã:é·ãã¯%uã§ããå¿è¦ãããã¾ãããé·ãã¯%uã§ãã %X/%Xã®ã¬ã³ã¼ããªãã»ãããç¡å¹ã§ã %2$X/%3$Xã®ãªã½ã¼ã¹ããã¼ã¸ã£ID %1$uãç¡å¹ã§ã %lu MBã³ãã¼ããå¿è¦ãããã¾ã(ã½ã¼ã¹ãã£ã¬ã¯ããªã®åè¨ãµã¤ãºã¯%lu MBã§ã) BKPIMAGE_HAS_HOLEãBKPIMAGE_IS_COMPRESSEDãè¨­å®ããã¦ãã¾ãããã%2$X/%3$Xã«ããã¦ãã­ãã¯ã¤ã¡ã¼ã¸é·ã%1$u å·»ãæ»ãã¯å¿è¦ããã¾ãã --write-recovery-confã«ã½ã¼ã¹ãµã¼ãæå ±(--source-server)ãæå®ããã¦ãã¾ãã ã½ã¼ã¹ãæå®ããã¦ãã¾ãã(--source-pgdata ã¾ãã¯ --source-server) ã¿ã¼ã²ãããã¼ã¿ãã£ã¬ã¯ããªãæå®ããã¦ãã¾ãã(--target-pgdata) --source-pgdataã--source-server ã¯ããããä¸æ¹ã®ã¿æå®å¯è½ã§ã ã¡ã¢ãªä¸è¶³ã§ã ã¡ã¢ãªä¸è¶³ã§ã
 block_id %uã%X/%Xã§ç¡å¹ã§ã ã­ã°ã»ã°ã¡ã³ã%3$sããªãã»ãã%4$uã®æç³»åID %1$u(%2$uã®å¾)ã¯é åºã«å¾ã£ã¦ãã¾ãã ã¿ã¼ã²ããã¯ã©ã¹ã¿ã§ã®postgresã³ãã³ãã®ã·ã³ã°ã«ã¦ã¼ã¶ã¢ã¼ãå®è¡ã«å¤±æãã¾ãã ã¿ã¼ã²ããã§WALãèª­ã¿è¾¼ãã§ãã¾ã ã½ã¼ã¹ãã¡ã¤ã«ãªã¹ããèª­ã¿è¾¼ãã§ãã¾ã ã¿ã¼ã²ãããã¡ã¤ã«ãªã¹ããèª­ã¿è¾¼ãã§ãã¾ã %2$X/%3$Xã®ã¬ã³ã¼ãé·%1$uãå¤§ãããã¾ã ç´åã®ãªã³ã¯%1$X/%2$Xãä¸æ­£ãªã¬ã³ã¼ãã%3$X/%4$Xã«ããã¾ã %X/%Xã®ã¬ã³ã¼ãã®ãµã¤ãºãç¡å¹ã§ã restore_commandãã·ã°ãã«ã«ããå¤±æãã¾ãã: %s ã¿ã¼ã²ããã¯ã©ã¹ã¿ã§restore_commandãè¨­å®ããã¦ãã¾ãã ã¿ã¤ã ã©ã¤ã³%3$uã®%1$X/%2$Xã«ããææ°ã®å±éãã§ãã¯ãã¤ã³ãããå·»ãæ»ãã¦ãã¾ã ã¿ã¤ã ã©ã¤ã³%3$uã®WALä½ç½®%1$X/%2$Xã§ä¸¡ãµã¼ããåå²ãã¦ãã¾ã ã½ã¼ã¹ã¨ã¿ã¼ã²ããã®ã¯ã©ã¹ã¿ãåä¸ã¿ã¤ã ã©ã¤ã³ä¸ã«ããã¾ã ã½ã¼ã¹ã¯ã©ã¹ã¿ã¨ã¿ã¼ã²ããã¯ã©ã¹ã¿ã¯ç°ãªãã·ã¹ãã ã®ãã®ã§ã ã½ã¼ã¹ãã¼ã¿ãã£ã¬ã¯ããªã¯ãããã«ã·ã£ãããã¦ã³ããã¦ããªããã°ãªãã¾ãã ã½ã¼ã¹ãã¡ã¤ã«ãªã¹ããç©ºã§ã ã½ã¼ã¹ãµã¼ãã¯ãªã«ããªã¢ã¼ãã§ãã£ã¦ã¯ãªãã¾ãã ã·ã³ããªãã¯ãªã³ã¯"%s"ã®åç§åãé·ããã¾ã ã¿ã¼ã²ãããã¼ã¿ãã£ã¬ã¯ããªãåæãã¦ãã¾ã å±¥æ­´ãã¡ã¤ã«åã®æ§æã¨ã©ã¼: %s ã¿ã¼ã²ãããµã¼ãã¯ãããã«ã·ã£ãããã¦ã³ããã¦ããªããã°ãªãã¾ãã ã¿ã¼ã²ãããµã¼ãã¯ãã¼ã¿ãã§ãã¯ãµã ãå©ç¨ãã¦ãããã¾ãã¯"wal_log_hints = on"ã§ããå¿è¦ãããã¾ã %X/%Xã§ contrecord ãã©ã°ãããã¾ãã  ã³ãã³ãã©ã¤ã³å¼æ°ãå¤ããã¾ã(åé ­ã¯"%s") ãã¡ã¤ã«"%s"ãèª­ã¿è¾¼ã¿ä¸­ã«æ³å®å¤ã®EOF æ³å®å¤ã®å¶å¾¡ãã¡ã¤ã«CRCã§ã æ³å®å¤ã®å¶å¾¡ãã¡ã¤ã«ã®ãµã¤ãº%dãæ³å®ã¯%d ãªã¢ã¼ããã¡ã¤ã«ã®ãã§ããä¸­ã®çµæã»ããã«æ³å®å¤ã®ãã¼ã¿å: %u %u %u äºæããªã"%1$s"ã®ãµã¤ãº: %3$lu ã§ã¯ãªã %2$lu ãªã¢ã¼ããã¡ã¤ã«ã®ãã§ããä¸­ã®çµæã«æ³å®å¤ã®NULLå¤ ãã£ã¬ã¯ããªã¾ãã¯ã·ã³ããªãã¯ãªã³ã¯"%s"ã«å¯¾ããæ³å®å¤ã®ãã¼ã¸ã®æ¸ãæãã§ã ã­ã°ã»ã°ã¡ã³ã%3$sããªãã»ãã%4$uã®ãã¼ã¸ã¢ãã¬ã¹%1$X/%2$Xã¯æ³å®å¤ã§ã ãªã¢ã¼ããã¡ã¤ã«ã®ãã§ããä¸­ã«æ³å®å¤ã®çµæå½¢å¼ ãªã¢ã¼ããã¡ã¤ã«ã®ãã§ããä¸­ã«æ³å®å¤ã®çµæã®é·ã ã¯ã¨ãªããæ³å®å¤ã®çµæã»ãã ãªã¢ã¼ããã¡ã¤ã«ã®ãã§ããä¸­ã«æ³å®å¤ã®çµæã»ãããµã¤ãº ãã¡ã¤ã«ãªã¹ãã®ãã§ããä¸­ã«æ³å®å¤ã®çµæã»ãã ãªã¢ã¼ããã¡ã¤ã«"%s"ã®ãã§ããä¸­ã«æ³å®å¤ã®çµæã»ãã ãªã¢ã¼ããã¡ã¤ã«ããã§ããä¸­ã«æ³å®å¤ã®çµæ: %s ãã¡ã¤ã«ãªã¹ããéä¿¡ä¸­ã«æ³å®å¤ã®çµæ: %s ç¾å¨ã®WALæ¿å¥ä½ç½®ã¨ãã¦èªè­ä¸å¯ã®çµæ"%s" è­¦å:  