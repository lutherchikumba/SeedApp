ή    *      l  ;   Ό      ¨     ©  #   Δ     θ  I   λ     5     R  '   h  '     *   Έ  C   γ  D   '  K   l  W   Έ  ;     .   L  1   {      ­      Ξ  .   ο  $        C  8   W  &     .   ·  J   ζ  '   1     Y  L   s  @   ΐ  5   	  E   7	  P   }	  >   Ξ	  0   
     >
  4   Z
  %   
  &   ΅
     ά
  !   τ
  !     X  8       0   €     Υ  M   Ψ     &     C  6   W  6     G   Ε  E     F   S  I     c   δ  D   H  F     J   Τ  -     -   M  H   {  #   Δ     θ  E   ψ  +   >  5   j  R      8   σ     ,  S   G  B     @   ή  R     [   r     Ξ  8   T       /   €      Τ  !   υ           *     K                                       &   "                                                  	       (   $                               
   %             !           #   '   *                         )       $_TD->{new} does not exist $_TD->{new} is not a hash reference %s If true, trusted and untrusted Perl code will be compiled in strict mode. PL/Perl anonymous code block PL/Perl function "%s" PL/Perl functions cannot accept type %s PL/Perl functions cannot return type %s Perl hash contains nonexistent column "%s" Perl initialization code to execute once when plperl is first used. Perl initialization code to execute once when plperlu is first used. Perl initialization code to execute when a Perl interpreter is initialized. SETOF-composite-returning PL/Perl function must call return_next with reference to hash cannot allocate multiple Perl interpreters on this platform cannot convert Perl array to non-array type %s cannot convert Perl hash to non-composite type %s cannot set generated column "%s" cannot set system attribute "%s" cannot use return_next in a non-SETOF function compilation of PL/Perl function "%s" couldn't fetch $_TD didn't get a CODE reference from compiling function "%s" didn't get a return item from function didn't get a return item from trigger function function returning record called in context that cannot accept type record ignoring modified row in DELETE trigger lookup failed for type %s multidimensional arrays must have array expressions with matching dimensions number of array dimensions (%d) exceeds the maximum allowed (%d) query result has too many rows to fit in a Perl array result of PL/Perl trigger function must be undef, "SKIP", or "MODIFY" set-returning PL/Perl function must return reference to array or use return_next set-valued function called in context that cannot accept a set trigger functions can only be called as triggers while executing PLC_TRUSTED while executing PostgreSQL::InServer::SPI::bootstrap while executing plperl.on_plperl_init while executing plperl.on_plperlu_init while executing utf8fix while parsing Perl initialization while running Perl initialization Project-Id-Version: plperl (PostgreSQL) 12
Report-Msgid-Bugs-To: pgsql-bugs@lists.postgresql.org
PO-Revision-Date: 2019-11-01 12:51+0900
Last-Translator: Ioseph Kim <ioseph@uri.sarang.net>
Language-Team: Korean Team <pgsql-kr@postgresql.kr>
Language: ko
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
 $_TD->{new} μμ $_TD->{new} μλ£νμ΄ ν΄μ μ°Έμ‘°κ° μλ %s trueλ‘ μ§μ νλ©΄, Perl μ½λκ° μκ²©ν κ΅¬λ¬Έ κ²μ¬λ‘ μ»΄νμΌ λ¨ PL/Perl μ΅λͺ μ½λ λΈλ­ "%s" PL/Perl ν¨μ PL/Perl ν¨μλ %s μλ£νμ μ¬μ©ν  μ μμ PL/Perl ν¨μλ %s μλ£νμ λ°νν  μ μμ Perl ν΄μμ μ‘΄μ¬νμ§ μλ "%s" μΉΌλΌμ΄ ν¬ν¨λμμ΅λλ€ plperl λͺ¨λμ΄ μ²μ μ¬μ©λ  λ μ€νν  Perl μ΄κΈ°ν μ½λ plperlu λͺ¨λμ΄ μ²μ μ¬μ©λ  λ μ€νν  Perl μ΄κΈ°ν μ½λ Perl μΈν°νλ¦¬ν°κ° μ΄κΈ°ν λ  λ μ€νν  Perl μ΄κΈ°ν μ½λ SETOF-composite-returning PL/Perl ν¨μλ return_next μμ ν΄μ μλ£νμ μ°Έμ‘°ν΄μΌ ν¨ μ΄ νλ«νΌμ μ¬λ¬ Perl μΈν°νλ¦¬ν°λ₯Ό μ¬μ©ν  μ μμ Perl λ°°μ΄νμ λΉλ°°μ΄ν %s μλ£νμΌλ‘ λ³νν  μ μμ Perl ν΄μ μλ£νμ λΉλ³΅ν© %s μλ£νμΌλ‘ λ³νν  μ μμ "%s" κ³μ°λ μΉΌλΌμ μ§μ ν  μ μμ "%s" μμ€ν μμ±μ μ§μ ν  μ μμ SETOF ν¨μκ° μλ κ²½μ°μλ return_next κ΅¬λ¬Έμ μΈ μ μμ "%s" PL/Perl ν¨μ μ»΄νλ μ΄μ $_TD λͺ» κ΅¬ν¨ "%s" ν¨μλ₯Ό μ»΄νμΌ νλ©΄μ μ½λ μ°Έμ‘°λ₯Ό κ΅¬ν  μ μμ ν¨μμμ λ°νν  ν­λͺ©μ λͺ» μ°Ύμ νΈλ¦¬κ±° ν¨μμμ λ°νν  ν­λͺ©μ λͺ» μ°Ύμ λ°ν μλ£νμ΄ recordμΈλ° ν¨μκ° κ·Έ μλ£νμΌλ‘ λ°ννμ§ μμ DELETE νΈλ¦¬κ±°μμλ λ³κ²½λ λ‘μ°λ λ¬΄μ ν¨ %s μλ£ν μ°ΎκΈ° μ€ν¨ λ€μ°¨μ λ°°μ΄μλ μΌμΉνλ μ°¨μμ΄ ν¬ν¨λ λ°°μ΄ μμ΄ μμ΄μΌ ν¨ μ§μ ν λ°°μ΄ ν¬κΈ°(%d)κ° μ΅λμΉ(%d)λ₯Ό μ΄κ³Όνμ΅λλ€ μΏΌλ¦¬ κ²°κ³Όκ° Perl λ°°μ΄μ λ΄κΈ°μλ λλ¬΄ λ§μ΅λλ€ PL/Perl νΈλ¦¬κ±° ν¨μμ κ²°κ³Όλ undef, "SKIP", "MODIFY" μ€ νλμ¬μΌ ν¨ μ§ν© λ°ν PL/Perl ν¨μλ λ°°μ΄ λλ return_next λ₯Ό μ¬μ©ν΄μ λ°νν΄μΌ ν¨ set-values ν¨μ(νμ΄λΈ λ¦¬ν΄ ν¨μ)κ° set μ μ μμ΄ μ¬μ©λμμ΅λλ€ (νμ΄λΈκ³Ό ν΄λΉ μ΄ alias μ§μ νμΈμ) νΈλ¦¬κ±° ν¨μλ νΈλ¦¬κ±°λ‘λ§ νΈμΆλ  μ μμ PLC_TRUSTED μ€ν μ€ PostgreSQL::InServer::SPI::bootstrap μ€ν μ€ plperl.on_plperl_init μ€ν μ€ plperl.on_plperlu_init μ€ν μ€ utf8fix μ€ν μ€ Perl μ΄κΈ°ν κ΅¬λ¬Έ λΆμ μ€ Perl μ΄κΈ°ν μ€ν μ€ 